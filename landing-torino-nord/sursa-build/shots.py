import asyncio, pathlib
from playwright.async_api import async_playwright
OUT = pathlib.Path('/tmp/claude-0/-home-user-iurieraileanu/shots'); OUT.mkdir(parents=True, exist_ok=True)
URL = 'file:///home/user/iurieraileanu/landing-torino-nord/PREVIZUALIZARE-TORINO-NORD-v4.html'
async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
        errs = []
        for name, w, hh, rm in [('desktop',1440,900,'reduce'),('tablet',820,1180,'reduce'),('mobil',390,844,'reduce')]:
            ctx = await b.new_context(viewport={'width':w,'height':hh}, device_scale_factor=1, reduced_motion=rm)
            p = await ctx.new_page()
            p.on('console', lambda m: errs.append((name,m.type,m.text)) if m.type=='error' else None)
            p.on('pageerror', lambda e: errs.append((name,'pageerror',str(e))))
            await p.goto(URL, wait_until='load')
            await p.wait_for_timeout(1200)
            # scroll pentru declanșarea apariției
            await p.evaluate("()=>new Promise(r=>{let y=0;const s=()=>{y+=700;window.scrollTo(0,y);if(y<document.body.scrollHeight)setTimeout(s,40);else{window.scrollTo(0,0);setTimeout(r,300);}};s();})")
            ow = await p.evaluate("()=>[document.documentElement.scrollWidth, window.innerWidth, document.body.scrollHeight]")
            print(name, 'scrollW/innerW/height =', ow, 'DEPĂȘIRE' if ow[0]>ow[1]+1 else 'fără derulare laterală')
            await p.screenshot(path=str(OUT/f'{name}-top.png'), full_page=False)
            if name=='desktop':
                for sel,fn in [('#vtn-cursuri','cursuri'),('#vtn-orar','orar'),('#vtn-spatii','spatii'),('#vtn-ansambluri','ansambluri'),('#vtn-media','media'),('#vtn-inscrieri','final')]:
                    el = await p.query_selector(sel)
                    if el: await el.scroll_into_view_if_needed(); await p.wait_for_timeout(500); await p.screenshot(path=str(OUT/f'sec-{fn}.png'))
                # test filtre
                await p.click('[data-vtn-coursefilters] [data-vtn-for="copii"]'); await p.wait_for_timeout(300)
                print('filtru copii →', await p.text_content('[data-vtn-coursecount]'))
                await p.click('[data-vtn-coursefilters] [data-vtn-for="toate"]')
                await p.click('[data-vtn-dayfilters] [data-vtn-for="miercuri"]'); await p.wait_for_timeout(300)
                print('filtru miercuri →', await p.text_content('[data-vtn-daycount]'),
                      '| rânduri vizibile:', await p.evaluate("()=>document.querySelectorAll('tr[data-vtn-day]:not([hidden])').length"))
                await p.click('[data-vtn-dayfilters] [data-vtn-for="all"]')
                # test lightbox
                await p.click('.vtn-lbbtn'); await p.wait_for_timeout(600)
                print('lightbox deschis:', await p.evaluate("()=>document.querySelector('.vtn-lb').classList.contains('vtn-open')"))
                await p.screenshot(path=str(OUT/'lightbox.png'))
                await p.keyboard.press('Escape'); await p.wait_for_timeout(300)
                print('lightbox închis:', not await p.evaluate("()=>document.querySelector('.vtn-lb').classList.contains('vtn-open')"))
            await ctx.close()
        print('ERORI JS:', errs if errs else 'niciuna')
        await b.close()
asyncio.run(main())

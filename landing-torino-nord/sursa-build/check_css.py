import asyncio
from playwright.async_api import async_playwright
URL='file:///home/user/iurieraileanu/landing-torino-nord/PREVIZUALIZARE-TORINO-NORD-v4.html'
async def main():
    async with async_playwright() as pw:
        b=await pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
        p=await b.new_page(viewport={'width':1440,'height':900})
        await p.goto(URL,wait_until='load'); await p.wait_for_timeout(500)
        res=await p.evaluate("""()=>{
          const out=[];
          const pick=sel=>{const e=document.querySelector(sel);if(!e)return null;
            const c=getComputedStyle(e);return {sel,color:c.color,bg:c.backgroundColor,border:c.borderColor,text:(e.textContent||'').trim().slice(0,28)};};
          ['.vtn-hero .vtn-btn--outline-light','.vtn-hero .vtn-btn--primary','.vtn-slogan',
           '.vtn-sec--deep .vtn-btn--light','.vtn-nav a','.vtn-filter','.vtn-ens-links a',
           '.vtn-final .vtn-btn--outline-light','.vtn-playlists a','.vtn-links a'].forEach(s=>{const r=pick(s);if(r)out.push(r);});
          return out;}""")
        for r in res: print(r)
        await b.close()
asyncio.run(main())

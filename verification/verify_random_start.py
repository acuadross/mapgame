
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for i in range(3):
            await page.goto('http://localhost:8000')
            
            # Esperar a que el botón de inicio esté habilitado
            await page.wait_for_selector('#start-game-btn:not([disabled])')
            
            # Hacer clic en el botón de inicio
            await page.click('#start-game-btn')
            
            # Esperar a que la sección del juego sea visible
            await page.wait_for_selector('#game-section:not(.hidden)')
            
            # Tomar una captura de pantalla del estado inicial del juego
            screenshot_path = f'verification/start_game_{i+1}.png'
            await page.screenshot(path=screenshot_path)
            print(f"Captura de pantalla guardada en: {screenshot_path}")
            
            # Reiniciar para la siguiente iteración
            await page.click('#restart-game-btn')
            await page.wait_for_selector('#setup-section:not(.hidden)')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

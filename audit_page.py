import os
from playwright.sync_api import sync_playwright

html_path = 'file:///' + os.path.abspath(r'd:\html pages\samruddhi\index.html').replace('\\', '/')
print('Loading:', html_path)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # 1. Desktop Audit (1280x900)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.goto(html_path)
    page.wait_for_timeout(600)
    page.screenshot(path=r'd:\html pages\samruddhi\screenshot_tab1_top.png')
    page.close()

    # 2. iPhone 14 / Mobile (390x844) Fluid Audit
    mobile_page = browser.new_page(viewport={'width': 390, 'height': 844})
    mobile_page.goto(html_path)
    mobile_page.wait_for_timeout(600)
    
    # Top hero & header
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_hero.png')
    print('Screenshot Mobile Hero saved')
    
    # Bento Grid
    mobile_page.locator('.bento-wrapper').scroll_into_view_if_needed()
    mobile_page.wait_for_timeout(300)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_bento.png')
    print('Screenshot Mobile Bento saved')
    
    # Tab Bar & Paper Sheet
    mobile_page.locator('.paper-sheet').scroll_into_view_if_needed()
    mobile_page.wait_for_timeout(300)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_paper.png')
    print('Screenshot Mobile Paper saved')
    
    # Switch to Tab 2
    mobile_page.locator('.tab-btn').nth(1).click()
    mobile_page.wait_for_timeout(400)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_tab2.png')
    print('Screenshot Mobile Tab 2 saved')
    
    # Scroll to Tab 2 Table
    mobile_page.locator('.comparison-table-wrapper').scroll_into_view_if_needed()
    mobile_page.wait_for_timeout(300)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_tab2_table.png')
    print('Screenshot Mobile Tab 2 Table saved')

    # Switch to Tab 3
    mobile_page.locator('.tab-btn').nth(2).click()
    mobile_page.wait_for_timeout(400)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_tab3.png')
    print('Screenshot Mobile Tab 3 saved')

    # Switch to Tab 4 & Achievement Card
    mobile_page.locator('.tab-btn').nth(3).click()
    mobile_page.wait_for_timeout(400)
    mobile_page.locator('.achievement-card').scroll_into_view_if_needed()
    mobile_page.wait_for_timeout(300)
    mobile_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_achievement.png')
    print('Screenshot Mobile Achievement saved')
    
    mobile_page.close()

    # 3. Small Android phone (360x780)
    small_page = browser.new_page(viewport={'width': 360, 'height': 780})
    small_page.goto(html_path)
    small_page.wait_for_timeout(500)
    small_page.screenshot(path=r'd:\html pages\samruddhi\screenshot_mobile_small_360.png')
    print('Screenshot Small Android 360 saved')
    small_page.close()

    print('Mobile Audit Complete!')
    browser.close()

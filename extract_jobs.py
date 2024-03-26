from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def format_string(s):
    words = s.split()
    formatted_words = []
    for word in words:
        formatted_word = word.capitalize()
        formatted_words.append(formatted_word)
    return ' '.join(formatted_words)

def scrape_jobs(job_title, locations):
    job_title = job_title.split()
    job_title = '+'.join(job_title)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        with open('job_data/job_data.txt', 'w', encoding="utf-8") as a:
            a.write("""<html>
            <body>
            """)
            for location in locations:
                url = f"https://www.google.com/search?q={job_title}+jobs+in+{location}&oq=dat&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyDQgCEAAYgwEYsQMYgAQyDQgDEAAYgwEYsQMYgAQyCggEEAAYsQMYgAQyCggFEAAYsQMYgAQyDQgGEAAYgwEYsQMYgAQyFggHEC4YgwEYxwEYsQMY0QMYgAQYigUyDQgIEAAYgwEYsQMYgAQyDQgJEAAYgwEYsQMYgATSAQgxMzA3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&ved=2ahUKEwjX9subt_GEAxVkslYBHctWDX4QudcGKAF6BAgXECk#htivrt=jobs&htidocid=MoOgGyBVCeJWoxBIAAAAAA%3D%3D&fpstate=tldetail"
                
                # go to url
                page.goto(url)
                page.wait_for_load_state("networkidle")
                for i in range(1,60):
                    page.evaluate('''() => {
                        const div = document.querySelector('.zxU94d.gws-plugins-horizon-jobs__tl-lvc[jsname="CaV2mb"]');
                        if (div) {
                            div.scrollTop = div.scrollHeight;
                        }
                    }''')
                    page.wait_for_load_state("networkidle")

                soup = BeautifulSoup(page.content(), features="lxml")

                # Find all 'li' tags
                li_tags = soup.find_all('li')
                for li_tag in li_tags:
                    a.write(str(li_tag))
                print(f"Search Completed for {location}.")
                time.sleep(1)
            a.write("""</body>
                </html>
                """
                )
        
        browser.close()
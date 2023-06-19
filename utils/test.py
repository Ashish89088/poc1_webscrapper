from bs4 import BeautifulSoup
import requests

cookies = {
    'li_sugr': '5a1f4ded-658f-4845-bb57-dfeb2903c240',
    'bcookie': '"v=2&400dc88e-04f1-44d2-8595-d7e00c788b0e"',
    'bscookie': '"v=1&202306051155574ee576dd-9e35-4446-8878-cbbe200a36c6AQFkEOv4EONslE6FGAnpM6SD046jqhQB"',
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg': '1',
    'aam_uuid': '82798693182611314252571546184832346037',
    '_gcl_au': '1.1.1022900601.1686718055',
    'timezone': 'Asia/Calcutta',
    'li_theme': 'light',
    'li_theme_set': 'app',
    'AnalyticsSyncHistory': 'AQIg-9O2lOmS3QAAAYi4QiUrT-MSg7Jyn3ewIZ9bu9vqXrmQH4NEI9Fmyh4A3mOVYOdzZTLKJIPOMTfNoNmn-g',
    '_guid': '413a636b-3553-46de-a305-0099a218b7ff',
    'lms_ads': 'AQFSIjcKjAhwLgAAAYi4Qia1i0DkCA_xFxqTnvcPXr3avHvyidKLIRfbM9FiSWSOxAb5tG_PStFlq3Gkurg34eUPTif3mQ_X',
    'lms_analytics': 'AQFSIjcKjAhwLgAAAYi4Qia1i0DkCA_xFxqTnvcPXr3avHvyidKLIRfbM9FiSWSOxAb5tG_PStFlq3Gkurg34eUPTif3mQ_X',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19523%7CMCMID%7C82255943459604222502549275561579222142%7CMCAAMLH-1687323324%7C3%7CMCAAMB-1687323324%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1686725724s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1454843921',
    'li_rm': 'AQHV4iBzetBfeAAAAYi4eADS7JjPz8KYsB1puZ5PT1XHVmHvUHWWRMedSrxXKxZita9SZa_H013yRRxAv3Jm-KyCnTpOHUbF1KifDj26SS2fZ-R18Cez_u0C',
    'li_g_recent_logout': 'v=1&true',
    'visit': 'v=1&M',
    'lang': 'v=2&lang=en-us',
    'g_state': '{"i_l":0}',
    'fcookie': 'AQExexIQTE1jEgAAAYi4eeD3kUtMUHIqZ3j-s3k8WloXk5mj0-QolBwP7qKlDGq7vKcE0g1sW0tI3ebTsZM4iXk2dyiETLyaj9sewpgVgnTPO9Sjtjzb9BSiiPIQ97QV0reUIXDgvXfyqvjxtmm1h1In1kM8BdctD4td7f00aTYHNgBH9I7LhWEZZ6faUQ7CpYAk56_zNoRfKIzuVAiWWFkMr-SkBa4QgZr8Qrh4UI6Yt0upmDYC1q3cR3Az731DAzYtpX1iwOln0LlNlvHiN6p6v/T9t/64bgs6H5UymDzH+wdF4CBlCWHdMXIilNLCy+kBpi6DMWeZ4w57n1h/yg==',
    'li_at': 'AQEDATF1dY0AkHHdAAABiLh54r8AAAGI3IZmv00AvxY2O9w8JCvNZjUDa5GmmYb8ZQtOLSJ1Y4J0e8IIN05aO_JjD0sTWI0Ah5paXfarPHA_YkER3NvNAEisWSQx2G9VKZRKMxPoTDEwsSTDKqr1CFHp',
    'liap': 'true',
    'JSESSIONID': '"ajax:6870926827375163338"',
    'fid': 'AQGizahzJLjNvgAAAYi4eeRpG5rI3xAD4a19hhw4eX_ejhRSy1s567cWy10f89LYHouBJpVnt-bjKA',
    'UserMatchHistory': 'AQLh0AhncT-RKgAAAYi4ee6bS9gkifMn01RqOuOtqEMvHRusQ1kyGiSeo0x8r4E8agj-327tu_2LBN7fwW2Chhw-6PzToTtPpjrMqYlV5IBKoZ-wISXS0s-2hx9kfNcHitsFZM8-vpznKa8WhheciRFpi_nMe8HaxvD7xq4ITJXcx7a3Ju05xllQnsU8qSwyKbpcYVfHhkfI1IhbIBcLFRhvtANfa3nsrSkn0HddqXfdB-RJgmr5pA5fj6yQtkK7teIKqLBP5XPQwYXBbUB8QAGxLCq5FYXuygyr-__wEBuGs9sv33sWvelGO8wcRk7bd_3yeB-CV4C-20XOtZfpUDoDyvgUK2o',
    'lidc': '"b=VB89:s=V:r=V:a=V:p=V:g=3291:u=558:x=1:i=1686722180:t=1686752040:v=2:sig=AQG_JTYdFAbhY5RKbLYYS8kGG7ZTrhCr"',
}

headers = {
    'authority': 'www.linkedin.com',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'li_sugr=5a1f4ded-658f-4845-bb57-dfeb2903c240; bcookie="v=2&400dc88e-04f1-44d2-8595-d7e00c788b0e"; bscookie="v=1&202306051155574ee576dd-9e35-4446-8878-cbbe200a36c6AQFkEOv4EONslE6FGAnpM6SD046jqhQB"; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=82798693182611314252571546184832346037; _gcl_au=1.1.1022900601.1686718055; timezone=Asia/Calcutta; li_theme=light; li_theme_set=app; AnalyticsSyncHistory=AQIg-9O2lOmS3QAAAYi4QiUrT-MSg7Jyn3ewIZ9bu9vqXrmQH4NEI9Fmyh4A3mOVYOdzZTLKJIPOMTfNoNmn-g; _guid=413a636b-3553-46de-a305-0099a218b7ff; lms_ads=AQFSIjcKjAhwLgAAAYi4Qia1i0DkCA_xFxqTnvcPXr3avHvyidKLIRfbM9FiSWSOxAb5tG_PStFlq3Gkurg34eUPTif3mQ_X; lms_analytics=AQFSIjcKjAhwLgAAAYi4Qia1i0DkCA_xFxqTnvcPXr3avHvyidKLIRfbM9FiSWSOxAb5tG_PStFlq3Gkurg34eUPTif3mQ_X; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19523%7CMCMID%7C82255943459604222502549275561579222142%7CMCAAMLH-1687323324%7C3%7CMCAAMB-1687323324%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1686725724s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1454843921; li_rm=AQHV4iBzetBfeAAAAYi4eADS7JjPz8KYsB1puZ5PT1XHVmHvUHWWRMedSrxXKxZita9SZa_H013yRRxAv3Jm-KyCnTpOHUbF1KifDj26SS2fZ-R18Cez_u0C; li_g_recent_logout=v=1&true; visit=v=1&M; lang=v=2&lang=en-us; g_state={"i_l":0}; fcookie=AQExexIQTE1jEgAAAYi4eeD3kUtMUHIqZ3j-s3k8WloXk5mj0-QolBwP7qKlDGq7vKcE0g1sW0tI3ebTsZM4iXk2dyiETLyaj9sewpgVgnTPO9Sjtjzb9BSiiPIQ97QV0reUIXDgvXfyqvjxtmm1h1In1kM8BdctD4td7f00aTYHNgBH9I7LhWEZZ6faUQ7CpYAk56_zNoRfKIzuVAiWWFkMr-SkBa4QgZr8Qrh4UI6Yt0upmDYC1q3cR3Az731DAzYtpX1iwOln0LlNlvHiN6p6v/T9t/64bgs6H5UymDzH+wdF4CBlCWHdMXIilNLCy+kBpi6DMWeZ4w57n1h/yg==; li_at=AQEDATF1dY0AkHHdAAABiLh54r8AAAGI3IZmv00AvxY2O9w8JCvNZjUDa5GmmYb8ZQtOLSJ1Y4J0e8IIN05aO_JjD0sTWI0Ah5paXfarPHA_YkER3NvNAEisWSQx2G9VKZRKMxPoTDEwsSTDKqr1CFHp; liap=true; JSESSIONID="ajax:6870926827375163338"; fid=AQGizahzJLjNvgAAAYi4eeRpG5rI3xAD4a19hhw4eX_ejhRSy1s567cWy10f89LYHouBJpVnt-bjKA; UserMatchHistory=AQLh0AhncT-RKgAAAYi4ee6bS9gkifMn01RqOuOtqEMvHRusQ1kyGiSeo0x8r4E8agj-327tu_2LBN7fwW2Chhw-6PzToTtPpjrMqYlV5IBKoZ-wISXS0s-2hx9kfNcHitsFZM8-vpznKa8WhheciRFpi_nMe8HaxvD7xq4ITJXcx7a3Ju05xllQnsU8qSwyKbpcYVfHhkfI1IhbIBcLFRhvtANfa3nsrSkn0HddqXfdB-RJgmr5pA5fj6yQtkK7teIKqLBP5XPQwYXBbUB8QAGxLCq5FYXuygyr-__wEBuGs9sv33sWvelGO8wcRk7bd_3yeB-CV4C-20XOtZfpUDoDyvgUK2o; lidc="b=VB89:s=V:r=V:a=V:p=V:g=3291:u=558:x=1:i=1686722180:t=1686752040:v=2:sig=AQG_JTYdFAbhY5RKbLYYS8kGG7ZTrhCr"',
    'csrf-token': 'ajax:6870926827375163338',
    'origin': 'https://www.linkedin.com',
    'referer': 'https://www.linkedin.com/feed/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'x-http-method-override': 'GET',
    'x-li-lang': 'en_US',
    'x-li-page-instance': 'urn:li:page:d_flagship3_feed;C4FCK+17TuahT1u3eTV0cA==',
    'x-li-track': '{"clientVersion":"1.12.7635","mpVersion":"1.12.7635","osName":"web","timezoneOffset":5.5,"timezone":"Asia/Calcutta","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.4700000286102295,"displayWidth":1921.29003739357,"displayHeight":1080.4500210285187}',
    'x-restli-protocol-version': '2.0.0',
}

data = 'ids=List(urn%3Ali%3Afsd_profile%3AACoAACqVQOkBkmAaBljKKs9w-tVJUDZkeYFGcbM,urn%3Ali%3Afsd_profile%3AACoAAAMKwlIBPzQscnwcN9gj59IkqV8QyYkvo3c)'

response = requests.post(
    'https://www.linkedin.com/voyager/api/messaging/dash/presenceStatuses',
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response)

webpage = requests.get(response, headers=headers)

soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)
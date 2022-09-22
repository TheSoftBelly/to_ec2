import requests
from bs4 import BeautifulSoup





BASE_URL = 'https://www.thebell.co.kr/free/content/article.asp?page=1&svccode=00'
res = requests.get(BASE_URL)
soup= BeautifulSoup(res.text , 'html.parser')
asideBox = soup.select('#contents > div.contentSection > div > div.asideBox > div.bestBox.tp2 > div > ul > li > ul > li > a')
asideBox_all_titles=[]
asideBox_hrefs = []
asideBox_call_hrefs = soup.find_all('a', class_='txtE')
for asideBox_href in asideBox_call_hrefs:
    asideBox_hrefs.append('https://www.thebell.co.kr/'+asideBox_href.attrs['href'])
for asideBox_title in asideBox:
    asideBox_titles=asideBox_title.text.strip()
    asideBox_all_titles.append(asideBox_titles)

# 첫페이지 신규 내용 크롤링
BASE_LIST_URL = 'https://www.thebell.co.kr/free/content/Article.asp?svccode=00'
res = requests.get(BASE_LIST_URL)
soup = BeautifulSoup(res.text , 'html.parser')
main_texts_titles = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > a > dt')
main_texts_contents = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > a > dd')
main_texts_reporters = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > dd > span.user')
main_texts_titles_list=[]
main_texts_contents_list=[]
main_texts_reporters_list=[]
for main_text in main_texts_titles:
    main_texts_titles_list.append(main_text.text)
for main_texts_content in main_texts_contents:
    main_texts_contents_list.append(main_texts_content.text)
for main_texts_reporter in main_texts_reporters:
    main_texts_reporters_list.append(main_texts_reporter.text.strip().replace('\xa0',' '))
BASE_href_URL = 'https://www.thebell.co.kr/free/content/Article.asp?svccode=00'
res = requests.get(BASE_LIST_URL)
soup = BeautifulSoup(res.text , 'html.parser')
main_texts_urls=soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > a')
main_texts_url_list = []
for main_texts_url in main_texts_urls:
    main_texts_url_list.append('https://www.thebell.co.kr/free/content/'+main_texts_url.attrs['href'])


#날씨 크롤링
weather_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
weather_res = requests.get(weather_url)
soup= BeautifulSoup(weather_res.text, 'html.parser')
weather_box = soup.find_all('div', class_="list_box _weekly_weather")
weather_today_daylist = []
weather_today_numdaylist = []
weather_like_todayresultslist = []
weather_today_temlist=[]
for weather_todays in weather_box:
    weather_today=weather_todays.select('ul > li > div > div.cell_date > span > strong')
    for weather_today_day in weather_today[0:3]:
        weather_today_daylist.append(weather_today_day.text)

for weather_today_num in weather_box:
    weather_today_numdays=weather_today_num.select('ul > li > div > div.cell_date > span > span')
    for weather_today_numday in weather_today_numdays[0:3]:
        weather_today_numdaylist.append(weather_today_numday.text)

for weather_likes in weather_box:
    weather_like = weather_likes.select('ul > li > div > div.cell_weather')
    for weather_like_todayresults in weather_like[0:3]:
        weather_like_todayresultslist.append(weather_like_todayresults.text.strip())

for weather_tems in weather_box:
    weather_today_tems = weather_tems.select('ul > li > div > div.cell_temperature > span')
    for weather_today_tem in weather_today_tems[0:3]:
        weather_today_temlist.append(weather_today_tem.text.strip())


asideBox_ul=''
main_content_div=''
main_content_div_list=[] 
#html로 바꾸기
for asideBox_num_for_ul in range(len(asideBox_hrefs)):
    asideBox_ul = asideBox_ul+'''<p style="font-size: 11px; font-family: Ubuntu, Helvetica, Arial;padding-top: 5px;"><a href='{asideBox_href}' style='color: black;'><span style="font-size: 16px;">{rank}. {asideBox_all_title}</span></a></p>'''.format(asideBox_href=asideBox_hrefs[asideBox_num_for_ul],asideBox_all_title=asideBox_all_titles[asideBox_num_for_ul],rank=asideBox_num_for_ul+1)

for main_num in range(len(main_texts_titles_list)):
    main_content_div_list.append(main_content_div+'''<div class="mj-column-per-50 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:50%;">

                                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                                                        <tbody>
                                                            <tr>
                                                                <td align="center" style="font-size:0px;padding:19px 19px 19px 19px;word-break:break-word;">

                                                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                                                        <tbody>
                                                                            <tr>
                                                                                <td style="width:261px;"></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>

                                                                    </td>
                                                                </tr>

                                                                <tr>
                                                                    <td align="left" style="font-size:0px;padding:0px 20px 0px 20px;word-break:break-word;">

                                                                        <div style="font-family:Merriweather, Georgia, serif;font-size:10px;line-height:1.5;text-align:left;color:#000000;">
                                                                            <h3 style="font-family: 'Merriweather', Georgia, serif; font-size: 20px;">{main_text_title}</h3>

                                                                            <p style="font-size: 11px; font-family: Ubuntu, Helvetica, Arial;">
                                                                                <span style="font-size:14px;">{main_text_content}    {main_text_reporter}</span>
                                                                            </p>
                                                                        </div>

                                                                    </td>
                                                                </tr>

                                                                <tr>
                                                                    <td align="left" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;">

                                                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" bgcolor="#59c7db" role="presentation" style="border:none;border-radius:none;cursor:auto;mso-padding-alt:10px 25px;background:#59c7db;" valign="middle">
                                                                                        <a href="{main_text_href}" style="display: inline-block; background: #59c7db; color: #ffffff; font-family: Ubuntu, Helvetica, Arial, sans-serif, Helvetica, Arial, sans-serif; font-size: 15px; font-weight: normal; line-height: 100%; margin: 0; text-decoration: none; text-transform: none; padding: 10px 25px; mso-padding-alt: 0px; border-radius: none;" target="_blank">더보기</a>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>

                                                                    </td>
                                                                </tr>

                                                            </tbody>
                                                        </table>

                                                    </div>'''.format(main_text_title=main_texts_titles_list[main_num],main_text_content=main_texts_contents_list[main_num],main_text_reporter=main_texts_reporters_list[main_num],main_text_href=main_texts_url_list[main_num]))

file = open('html_test.html','w',encoding='UTF-8')
file_contents='''<body style="background-color:#FFFFFF;">

    <div style="background-color:#FFFFFF;">

        <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
        cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
        style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
        <![endif]-->

        <div style="margin:0px auto;max-width:600px;">

            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:0px 0px 0px 0px;text-align:center;">
                            <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                            cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:600px;" >
                            <![endif]-->

                            <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                                    <tbody>
                                        <tr>
                                            <td align="center" style="font-size:0px;padding: 0px 9px 0px 9px;word-break:break-word;">

                                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                                    <tbody>
                                                        <tr>
                                                            <td style="width:180px;">

                                                                <img height="auto" src="https://cdn.freelogodesign.org/files/9856f3e8550f4d0db28865e86459fd71/thumb/logo_200x200.png?v=0" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="180"></td>
                                                            </tr>
                                                        </tbody>
                                                    </table>

                                                </td>
                                            </tr>

                                            <tr>
                                                <td style="font-size:0px;padding:20px 22px;padding-top:20px;word-break:break-word;">

                                                    <p style="font-family: Ubuntu, Helvetica, Arial; border-top: solid 1px #ACACAC; font-size: 1; margin: 0px auto; width: 100%;"></p>

                                                    <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                                    cellspacing="0" style="border-top:solid 1px #ACACAC;font-size:1;margin:0px
                                                    auto;width:556px;" role="presentation" width="556px" > <tr> <td
                                                    style="height:0;line-height:0;"> &nbsp; </td> </tr> </table> <![endif]-->

                                                </td>
                                            </tr>

                                        </tbody>
                                    </table>

                                </div>

                                <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>

            <!--[if mso | IE]> </td> </tr> </table> <table align="center" border="0"
            cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" > <tr>
            <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
            <![endif]-->

            <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px;">

                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
                    <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:12px 0px 12px 0px;text-align:center;">
                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                cellspacing="0"> <tr> <td class="" style="vertical-align:middle;width:600px;" >
                                <![endif]-->

                                <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">

                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">

                                        <tbody>

                                            <tr>
                                                <td align="center" style="font-size:0px;padding:0px 20px 0px 20px;word-break:break-word;">

                                                    <div style="font-family:Merriweather, Georgia, serif;font-size:10px;line-height:1.5;text-align:center;color:#000000;">
                                                        <h1 style="font-family: 'Merriweather', Georgia, serif; font-size: 32px; color: #4E4E4E;">
                                                            <em>NEWS RANK</em>
                                                        </h1>
                                                    </div>

                                                </td>
                                            </tr>

                                            <tr>
                                                <td style="font-size:0px;padding:20px 22px;padding-top:20px;word-break:break-word;">

                                                    <p style="font-family: Ubuntu, Helvetica, Arial; border-top: solid 1px #ACACAC; font-size: 1; margin: 0px auto; width: 100%;"></p>

                                                    <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                                    cellspacing="0" style="border-top:solid 1px #ACACAC;font-size:1;margin:0px
                                                    auto;width:556px;" role="presentation" width="556px" > <tr> <td
                                                    style="height:0;line-height:0;"> &nbsp; </td> </tr> </table> <![endif]-->

                                                </td>
                                            </tr>

                                            <tr>
                                                <td style="font-size:0px;padding:0px 43px 0px 43px;word-break:break-word;">

                                                    <div style="font-family:Merriweather, Georgia, serif;font-size:10px;line-height:1.5;color:#000000;">
                                                        {asideBox_ul}
                                                    </div>

                                                </td>
                                            </tr>

                                            <tr>
                                                <td style="font-size:0px;padding:20px 22px;padding-top:20px;word-break:break-word;">

                                                    <p style="font-family: Ubuntu, Helvetica, Arial; border-top: solid 1px #ACACAC; font-size: 1; margin: 0px auto; width: 100%;"></p>

                                                    <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                                    cellspacing="0" style="border-top:solid 1px #ACACAC;font-size:1;margin:0px
                                                    auto;width:556px;" role="presentation" width="556px" > <tr> <td
                                                    style="height:0;line-height:0;"> &nbsp; </td> </tr> </table> <![endif]-->

                                                </td>
                                            </tr>

                                        </tbody>
                                    </table>

                                </div>

                                <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                            </td>
                        </tr>
                    </tbody>
                </table>

            </div>

            <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td>

                            <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                            cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                            style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                            <![endif]-->

                            <div style="margin:0px auto;max-width:600px;">

                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                    <tbody>
                                        <tr>
                                            <td style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;">
                                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:300px;" >
                                                <![endif]-->

                                                {main_content_div_list_zero}

                                                    <!--[if mso | IE]> </td> <td class="" style="vertical-align:top;width:300px;" >
                                                    <![endif]-->
                                                    {main_content_div_list_one}
                                                        <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>

                                    </div>

                                    <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                </td>
                            </tr>
                        </tbody>
            </table>

            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td>

                            <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                            cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                            style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                            <![endif]-->

                            <div style="margin:0px auto;max-width:600px;">

                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                    <tbody>
                                        <tr>
                                            <td style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;">
                                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:300px;" >
                                                <![endif]-->

                                                    {main_content_div_list_two}
                                                    <!--[if mso | IE]> </td> <td class="" style="vertical-align:top;width:300px;" >
                                                    <![endif]-->
                                                    {main_content_div_list_three}

                                                        <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>

                                    </div>

                                    <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                </td>
                            </tr>
                        </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td>

                            <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                            cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                            style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                            <![endif]-->

                            <div style="margin:0px auto;max-width:600px;">

                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                    <tbody>
                                        <tr>
                                            <td style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;">
                                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:300px;" >
                                                <![endif]-->

                                                    {main_content_div_list_four}
                                                    <!--[if mso | IE]> </td> <td class="" style="vertical-align:top;width:300px;" >
                                                    <![endif]-->

                                                        {main_content_div_list_five}
                                                        <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>

                                    </div>

                                    <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                </td>
                            </tr>
                        </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                    <tr>
                        <td>

                            <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                            cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                            style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                            <![endif]-->

                            <div style="margin:0px auto;max-width:600px;">

                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                    <tbody>
                                        <tr>
                                            <td style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;">
                                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:300px;" >
                                                <![endif]-->

                                                    {main_content_div_list_six}
                                                    <!--[if mso | IE]> </td> <td class="" style="vertical-align:top;width:300px;" >
                                                    <![endif]-->

                                                        {main_content_div_list_seven}
                                                        <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>

                                    </div>

                                    <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                </td>
                            </tr>
                        </tbody>
            </table>
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                            <tr>
                                <td>

                                    <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                    cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                                    style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                                    <![endif]-->

                                    <div style="margin:0px auto;max-width:600px;">

                                        <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                            <tbody>
                                                <tr>
                                                    <td style="direction:ltr;font-size:0px;padding:27px 0px 27px 0px;text-align:center;">
                                                        <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                        cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:300px;" >
                                                        <![endif]-->

                                                            {main_content_div_list_eight}
                                                            <!--[if mso | IE]> </td> <td class="" style="vertical-align:top;width:300px;" >
                                                            <![endif]-->

                                                                {main_content_div_list_nine}
                                                                <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>

                                            </div>

                                            <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                        </td>
                                    </tr>
                                </tbody>
            </table>

            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                <tbody>
                                    <tr>
                                        <td>

                                            <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                            cellspacing="0" class="" style="width:600px;" width="600" > <tr> <td
                                            style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                                            <![endif]-->

                                            <div style="margin:0px auto;max-width:600px;">

                                                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                                                    <tbody>
                                                        <tr>
                                                            <td style="direction:ltr;font-size:0px;padding:9px 0px 9px 0px;text-align:center;">
                                                                <!--[if mso | IE]> <table role="presentation" border="0" cellpadding="0"
                                                                cellspacing="0"> <tr> <td class="" style="vertical-align:top;width:600px;" >
                                                                <![endif]-->

                                                                <div class="mj-column-per-100 outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">

                                                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">

                                                                        <tbody>
                                                                            <tr>
                                                                                <td style="font-size:0px;padding:20px 22px;padding-top:20px;word-break:break-word;">

                                                                                    <p style="font-family: Ubuntu, Helvetica, Arial; border-top: solid 1px #ACACAC; font-size: 1; margin: 0px auto; width: 100%;"></p>

                                                                                    <!--[if mso | IE]> <table align="center" border="0" cellpadding="0"
                                                                                    cellspacing="0" style="border-top:solid 1px #ACACAC;font-size:1;margin:0px
                                                                                    auto;width:556px;" role="presentation" width="556px" > <tr> <td
                                                                                    style="height:0;line-height:0;"> &nbsp; </td> </tr> </table> <![endif]-->

                                                                                </td>
                                                                            </tr>

                                                                        </tbody>
                                                                    </table>

                                                                </div>

                                                                <!--[if mso | IE]> </td> </tr> </table> <![endif]-->
                                                            </td>
                                                        </tr>
                                                    </tbody>
                                                </table>

                                            </div>

                                            <!--[if mso | IE]> </td> </tr> </table> <![endif]-->

                                        </td>
                                    </tr>
                                </tbody>
            </table>

        </div>

    </body>'''.format(asideBox_ul=asideBox_ul,main_content_div_list_zero=main_content_div_list[0],main_content_div_list_one=main_content_div_list[1],main_content_div_list_two=main_content_div_list[2],main_content_div_list_three=main_content_div_list[3],main_content_div_list_four=main_content_div_list[4],main_content_div_list_five=main_content_div_list[5],main_content_div_list_six=main_content_div_list[6],main_content_div_list_seven=main_content_div_list[7],main_content_div_list_eight=main_content_div_list[8],main_content_div_list_nine=main_content_div_list[9])

file.write(file_contents)
file.close()

#메일 보내는 라이브러리 / send_who 에는 이메일 주소를 string 으로 보내준다 
#만약에 리스트라면 ", ".join(send_who) 를 하지만 그게 아니라면 그냥 '메일, 메일'형태로 보내줌
#여기서 핵심은 ,후에 한번 뛰우는거다.

def mail_form(send_who):
    SMTP_SEVER = 'smtp.naver.com'
    SMTP_PORT = 465
    SMTP_USER = 'jjoon1024@naver.com'
    SMTP_PASSWORD = open('/home/ubuntu/workspace/to_ec2/email_config.txt','r').readline().rstrip()

    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText

    #편지봉투 만들기
    msg = MIMEMultipart('alternative')
    #html 파일 열기
    f=open("html_test.html", 'r')


    #편지 내용 = html파일을 읽어온 것
    contents = f.read()

    msg['From'] = SMTP_USER 
    msg['To'] = '내가 사랑하고 나를 사랑하는 모두에게'
    msg['Subject'] = 'NEWSBOY .made_by_HyoJoon'

    text = MIMEText(contents,'html')

    msg.attach(text)

    import smtplib

    try:
        smtp=smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
        print('메일 서버 접속 성공')
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        print('로그인 성공')
        smtp.sendmail(SMTP_USER,send_who , msg.as_string())
        print('이메일 발송 성공!')


    except Exception as e:
        print('###에러발생###')
        print(e)
    finally:
        smtp.close()
        print('파이널리')

file = open("/home/ubuntu/workspace/to_ec2/email_list.txt", "r")
strings = file.readlines()
file.close()

mail_form(strings)


import json
import re
import urllib
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup as soup


class IndianKanoonScrapper:
    """
    API for retrieving judgments from IndianKanoon.

    Methods:
        get_judgment_txt_from_url(url): Retrieves the judgment text from the judgment at the given URL.
    """

    def get_judgment_txt_from_url(self, url):
        """
        Retrieves the judgment text from the judgment at the given URL.

        Args:
            url (str): The URL of the judgment.

        Returns:
            str: The judgment text.
        """
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        try:
            webpage = urlopen(req, timeout=10).read()
            page_soup = soup(webpage, "html.parser")

            preamble_tags = page_soup.find_all('pre')
            preamble_txt = ''.join([i.text for i in  preamble_tags if i.get('id') is not None and i['id'].startswith('pre_')])
            judgment_txt_tags = page_soup.find_all(['p','blockquote'])
            judgment_txt = ''
            for judgment_txt_tag in judgment_txt_tags:
                tag_txt=''
                if judgment_txt_tag.get('id') is not None and (judgment_txt_tag['id'].startswith('p_') or
                                                           judgment_txt_tag['id'].startswith('blockquote_')):
                    for content in judgment_txt_tag.contents:
                        if isinstance(content,Tag):
                            if not(content.get('class') is not None and  'hidden_text' in content['class'] ):
                                tag_txt = tag_txt + content.text
                        else:
                            tag_txt = tag_txt + str(content)
                tag_txt = re.sub(r'\s+(?!\s*$)',' ',tag_txt) ###### replace the multiple spaces, newlines with space except for the ones at the end.
                tag_txt = re.sub(r'([.\"\?])\n',r'\1 \n\n',tag_txt) ###### add the extra new line for correct sentence breaking in spacy

                judgment_txt = judgment_txt + tag_txt
            judgment_txt = re.sub(r'\n{2,}', '\n\n', judgment_txt)
            judgment_txt = preamble_txt + judgment_txt

        except:
            judgment_txt=''

        return judgment_txt


if __name__ == "__main__":
    api = IndianKanoonScrapper()
    judgment_txt_output = api.get_judgment_txt_from_url('https://indiankanoon.org/doc/103570654')
    print(judgment_txt_output)

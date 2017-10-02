from django.db import models
from tinymce.models import HTMLField
import json, requests
import re

class Text(models.Model):
    content = HTMLField()
    tr_content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)

    def add_tr(self, c, tr_c):


        return 0


class Paragraph(models.Model):
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    content = models.TextField()
    tr_content = models.TextField()
    order_id = models.IntegerField()

    pub_date = models.DateTimeField(auto_now_add=True)

    def cleanhtml(self):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', self.content)
        return cleantext


class Sentence(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    text_id = models.IntegerField()
    text_order_id = models.IntegerField()
    content = models.TextField()
    tr_content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)

    def translate_words(self, word, from_lang):
        query = word
        max_count = "25"
        re_ceviri = json.loads(
            requests.get("http://cevir.ws/v1?q=" + query + "&m=" + max_count + "&p=exact&l=" + from_lang).text)
        print(re_ceviri["control"]["results"])
        if re_ceviri["control"]["results"] != 0:
            ret = ""
            for i in re_ceviri["word"]:
                ret += i["desc"].split(";")[0] + " "
            return ret
        else:
            return "Ceviri Bulunamadi"

    def __str__(self):
        return self.content
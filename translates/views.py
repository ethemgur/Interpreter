from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from mtranslate import translate
from .forms import TextForm
from .models import Text, Sentence, Paragraph
from .sentence_split import split_into_sentences, cleanhtml
from bs4 import BeautifulSoup

def index(request):
    from_lang = "en"
    to_lang = "tr"
    output = translate("I'm really good.", to_lang, from_lang)
    return render(request, 'translates/index.html', {"output":output})

def new(request):
    form = TextForm()
    return render(request, "translates/new.html", {"form":form})

def create(request):
    form = TextForm(request.POST)
    if form.is_valid():
        print("The form is valid!")
        text = form.save()
        print(text)

        # Soup part uncompleted
        soup = BeautifulSoup(text.content)
        paragraphs = list(str(x) for x in soup.findAll('p'))
        print(paragraphs)

        # Creating paragraphs and sentences
        j = 0
        k = 0
        for p in paragraphs:
            pa = text.paragraph_set.create(content=cleanhtml(p), order_id=j)
            sentences = split_into_sentences(pa.content)
            print(pa, j)
            i = 0
            for s in sentences:
                pa.sentence_set.create(content=s, order_id=i, text_order_id=k, text_id=text.id)
                i += 1
                k += 1
                print(s, i)
            j += 1

        return HttpResponseRedirect(reverse('translates:interpret', args=(text.id,0,)))
    else:
        print("The form is NOT valid!")
        return HttpResponseRedirect(reverse('translates:new'))

def interpret(request, text_id, sentence_id):
    text = get_object_or_404(Text, pk=text_id)
    sentence = Sentence.objects.get(text_id=text_id, text_order_id=sentence_id)
    if request.method == "POST":
        sentence.tr_content = request.POST['tr_content']
        if sentence.save():
            return HttpResponseRedirect(reverse('translates:interpret', args=(text_id,int(sentence_id)+1,)))
        else:
            return HttpResponseRedirect(reverse('translates:interpret', args=(text_id, sentence_id,)))
    else:
        # Sentence Translation
        from_lang = "en"
        to_lang = "tr"
        gtranslation = translate(sentence.content, to_lang, from_lang)

        # Word Translation
        words={}
        split_sentence = sentence.content.split()
        for s in split_sentence:
            words[s] = sentence.translate_words(s, from_lang)

        context = {"text":text, "sentence":sentence, "text_id":text_id, "sentence_id":sentence_id, "gtranslation":gtranslation, "words":words}

        return render(request, "translates/interpret.html", context)


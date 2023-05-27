from django.shortcuts import render
import openai

openai.api_key = "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"
# Create your views here.
from .forms import DictForm

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



def dict_view(request):
    if request.method == "POST":
        form = DictForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            language = form.cleaned_data['language']


            prompt = f"Translate text delimited by <> brackets into {language} language. <{text}>"

            completion = get_completion(prompt)

            return render(request, 'dict/dict.html', {'form': form, 'completion': completion})
    else:
        form = DictForm()
    return render(request, 'dict/dict.html', {'form': form})

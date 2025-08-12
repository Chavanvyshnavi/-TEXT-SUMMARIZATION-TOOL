# hybrid_summarizer.py
try:
    from transformers import pipeline
    use_transformers = True
except ModuleNotFoundError:
    use_transformers = False

from simple_summarizer import summarize  # the function from the previous file

text = "..."  # your long article here

if use_transformers:
    summarizer = pipeline("summarization")  # may download a model the first run
    out = summarizer(text, max_length=120, min_length=30, do_sample=False)
    print(out[0]["summary_text"])
else:
    print("transformers not installed — using simple local summarizer.")
    print(summarize(text, n_sentences=3))

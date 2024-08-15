from gpt4all import GPT4All
model = GPT4All("C:\\LLM-Models\\kunoichi\\kunoichi-dpo-v2-7b.Q5_K_M.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session():
    print(model.generate("Я хочу играть в компьютерные игры в разрешении FullHD с 60фпс, какие варианты комплектующих мне подойдут?", max_tokens=1024))
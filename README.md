# Codeslator - Translate Codes from One Programming Language to Another

```
Author: Han-Elliot Phan
Email: hanelliotphan@gmail.com

Last update: February 20, 2025
```

## Brief Description
This project is to take in a file of code and translate it into another language 
that is optimized and executable.

## Architecture
This project uses the OpenAI's GPT-4o and the Anthropic's Claude 3.5 
Sonnet models to ensure the executability of the translated code while still 
guaranteeing the optimization of the code.

For more information about the model, please read the following documentation:
- [OpenAI's GPT-4o](https://platform.openai.com/docs/guides/text-generation)
- [Anthropic's Claude 3.5 Sonnet](https://docs.anthropic.com/en/api/messages-streaming)

## Instructions of Use
First, determine the model you would like to use with the following options:
- `gpt-4o`: OpenAI's GPT-4o
- `claude-3`: Anthropic's Claude 3.5 Sonnet

Second, acquire the API keys for the supported models above and export the keys 
as below:
```bash
$ export OPENAI_API_KEY=<you OpenAI API key>
$ export ANTHROPIC_API_KEY=<you Anthropic API key>
```

Next, install required packages via `pip` command
```bash
$ pip install -r requirements.txt
```

Finally, run the `main.py` script to execute the software
```bash
$ python ./codeslator/src/main.py -f <your code filepath> -fl <your code language> -tl <language to translate your code to> -m <your desired model>
```
where
- `-f / --file`: The filepath of the code to translate.
- `-fl / --from_language`: The language to translate the code from (please see 
the supported languaged below).
- `-tl / --to_language`: The language to translate the code to.
- `-m / --model`: The model to use for the code translation.

You will find the result code file under the `./files` folder.

**Supported Languages:**
- C
- C++
- C#
- Dart
- Elixir
- Erlang
- Go/Golang
- Java
- JavaScript
- Kotlin
- PHP
- Python2/Python3
- Racket
- Ruby
- Rust
- Scala
- Swift
- TypeScript

## Dedication
I dedicate this hard-work commitment to myself, my mother, my best friend 
Ha-Phuong and those that have imprinted in my heart. I hope that I have made 
you all truly proud of me.

## References
- [OpenAI's GPT-4o](https://platform.openai.com/docs/guides/text-generation)
- [Anthropic's Claude 3.5 Sonnet](https://docs.anthropic.com/en/api/messages-streaming)
#importing necessary library
import argparse
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#provide the template
template='''
I want you to summarise the text provided to you

content:{content}
'''
#defining which model we plan on using
model=OllamaLLM(model="llama3.2")

#create a prompt template object
prompt=ChatPromptTemplate.from_template(template)

#chain the prompt with the model   
chain=prompt | model

def summary(content):
    return chain.invoke({"content":content})

def main():
    parser=argparse.ArgumentParser(description="Summarise text or file content")
    parser.add_argument('-t', '--textfile', type=str, help="Path to the text file to summarize.")
    parser.add_argument('-s', '--string', type=str, help="Text string to summarize.")

    args=parser.parse_args()

    content=None
    if args.textfile:
        try:
            with open(args.textfile, "r", encoding="utf-8") as file:
                content=file.read()
        except FileNotFoundError:
            print(f"Error the {args.textfile} wasn't found")
    elif args.string:
        content=args.string
    
    else:
        print("Error: You must provide either a text file (-t) or a text string (-s).")
        return
    
    result=summary(content)
    print(f"\nSummary:\n{result}")

if __name__ == "__main__":
    main()
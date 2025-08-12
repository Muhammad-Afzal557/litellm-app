import os
from litellm import  completion
from dotenv import  load_dotenv

load_dotenv()


def main ():
    api_key = os.getenv ("Gemini_Api_Key")

    response = completion(
        model = "gemini/gemini-2.0-flash",
        messages = [
            {
                "role"  : "user" ,
                  "content" : "Who is the founder of pakitsan?",

            }
        ]
    )
    print (response ['choices'][0] ['message']['content'])

if __name__ ==  "__main__" :
    main()
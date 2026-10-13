from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

 

# load_dotenv()
load_dotenv(override=True)


def main() -> None:
    print("Hello from langchain-course!")
    information = """Nandamuri Balakrishna (born 10 June 1960), also known as Balayya and N.B.K., is an Indian actor, producer, politician and philanthropist known for his works in Telugu cinema.[1][2][3][4] The son of Indian matinée idol and former Chief Minister of Andhra Pradesh N. T. Rama Rao, Balakrishna made his debut as a child artist at the age of 14 with the film Tatamma Kala (1974).[5][6] Balakrishna is an elected member of the Andhra Pradesh Legislative Assembly from Hindupur constituency since 2014.[7] He is the Chairman of Basavatarakam Indo-American Cancer Hospital and Research Institute.[8]

Known for his work as a dancer and an actor in Telugu cinema, Balakrishna was the chief guest at the 43rd IFFI.[9] In 2025, the Government of India honoured him with third-highest civilian award in India, the Padma Bhushan.[10][11] In the same year, He entered the World Book of Records for completing 50 years in films.[12] He was also awarded the Special Recognition for Contribution to Bharatiya Cinema at the 56th IFFI.[13] He is a recipient of three state Nandi Awards, two SIIMA Awards, and an IIFA Award.[14]

Balakrishna starred in more than hundred feature films in a variety of roles.[15] He achieved commercial success, with works such as Sahasame Jeevitham (1984), Janani Janmabhoomi (1984), Mangammagari Manavadu (1984), Apoorva Sahodarulu (1986), Muvva Gopaludu (1987), Muddula Mavayya (1989), Nari Nari Naduma Murari (1990), Lorry Driver (1990), Aditya 369 (1991), Rowdy Inspector (1992), Bangaru Bullodu (1993), Bhairava Dweepam (1994), Peddannayya (1997), Samarasimha Reddy (1999), Narasimha Naidu (2001), Lakshmi Narasimha (2004), Simha (2010), Legend (2014), Akhanda (2021), Veera Simha Reddy (2023), Bhagavanth Kesari (2023) and Daaku Maharaaj (2025).

Balakrishna experimented with biographical, historical and hagiographical films. He played poet Vemulawada Bheemakavi in Vemulawada Bheemakavi (1976); Abhimanyu in Daana Veera Soora Karna (1977); Jahangir in Akbar Salim Anarkali (1979); Narada in Sri Tirupati Venkateswara Kalyanam (1979); Sidda in Srimadvirat Veerabrahmendra Swami Charitra (1984); Krishnadevaraya in Aditya 369 (1991); Satya Harischandra and Dushyanta in Brahmarshi Viswamitra (1991); Lord Krishna and Arjuna in Sri Krishnarjuna Vijayam (1996); Pundarika in Pandurangadu (2008); N. T. Rama Rao in NTR: Mahanayakudu (2019) and NTR: Kathanayakudu (2019); and Lord Rama in Sri Rama Rajyam (2011) featured at the 42nd IFFI.[16] In his 100th film, he played Gautamiputra Satakarni, second-century ruler of the Satavahana dynasty in the epic war film Gautamiputra Satakarni (2017).[17][18] Balakrishna has received three state Nandi Awards for Best Actor for his works in Narasimha Naidu (2001), Simha (2010), and Legend (2014).[19]"""
    summary_template = """
Given the information {information}, about a person I want you to create: 
1. A short summary
2. Two interesting facts about them"""

    summary_prompt_template = ChatPromptTemplate.from_template(summary_template)
    # summary_prompt_template = PromptTemplate.from_template(summary_template)
    llm = ChatAnthropic(model = "claude-haiku-5-5")
    chain = summary_prompt_template | llm
    response = chain.invoke(input = {"information": information})
    print(response.content)


if __name__ == "__main__":
    main()

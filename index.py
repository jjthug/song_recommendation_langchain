from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.llms import OpenAI

from langchain.vectorstores import DeepLake


def create_db(dataset_path: str, json_filepath: str) -> DeepLake:

    with open(json_filepath, "r") as f:

        data = json.load(f)


    texts = []

    metadatas = []


    for movie, lyrics in data.items():

        for lyric in lyrics:

            texts.append(lyric["text"])

            metadatas.append(

                {

                    "movie": movie,

                    "name": lyric["name"],

                    "embed_url": lyric["embed_url"],

                }

            )


    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")


    db = DeepLake.from_texts(

        texts, embeddings, metadatas=metadatas, dataset_path=dataset_path

    )


    return db


def load_db(dataset_path: str, *args, **kwargs) -> DeepLake:
    db = DeepLake(dataset_path, *args, **kwargs)
    return db



# postprocessing

def filter_scores(matches: Matches, th: float = 0.8) -> Matches:

    return [(doc, score) for (doc, score) in matches if score > th]


matches = filter_scores(matches, 0.8)


#normalize


def normalize_scores_by_sum(matches: Matches) -> Matches:
    scores = [score for _, score in matches]
    tot = sum(scores)
    return [(doc, (score / tot)) for doc, score in matches]


# random sample

docs, scores = zip(*matches)
docs = weighted_random_sample(
    np.array(docs), np.array(scores), n=number_of_displayed_songs
).tolist()
for doc in docs:
    print(doc.metadata["name"])

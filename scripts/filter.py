from pathlib import Path
import srsly
import yaml
import pandas as pd

FILTER_TRAIN = True
FILTER_EVAL = False


def filter(input_path, output_path, filter_data_flag):
    data = (doc for doc in srsly.read_jsonl(input_path))
    data = [x for x in data]
    # filter
    print(f"Amount records for {input_path.name} before filtering - {len(data)}")
    if filter_data_flag:
        filtered_data = [x for x in data if len(x['text'])<2000]
    else:
        filtered_data = data
    print(f"Amount records for {input_path.name} after filtering - {len(filtered_data)}")
    srsly.write_jsonl(output_path, filtered_data)


def main(
):
    # Read params
    with open('params.yaml', "r") as f:
        params = yaml.safe_load(f)
    #Train 
    train_input_path = Path(f"assets/{params['vars']['train']}_raw.jsonl")
    train_output_path = Path(f"assets/{params['vars']['train']}.jsonl")
    filter(train_input_path, train_output_path, True)
    #Eval
    eval_input_path = Path(f"assets/{params['vars']['dev']}_raw.jsonl")
    eval_output_path = Path(f"assets/{params['vars']['dev']}.jsonl")
    filter(eval_input_path, eval_output_path, False)


if __name__ == "__main__":
    main()

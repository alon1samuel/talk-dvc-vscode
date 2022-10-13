import yaml
import shutil
import os

def main():
    # Read params
    with open('params.yaml', "r") as f:
        params = yaml.safe_load(f)
    # Train
    train_raw_path = f"assets/{params['vars']['train']}_original.jsonl"
    train_input_path = f"assets/{params['vars']['train']}_raw.jsonl"
    if not os.path.exists(train_input_path): 
        shutil.copy(train_raw_path, train_input_path)
    # Eval
    eval_raw_path = f"assets/{params['vars']['dev']}_original.jsonl"
    eval_input_path = f"assets/{params['vars']['dev']}_raw.jsonl"
    if not os.path.exists(eval_input_path): 
        shutil.copy(eval_raw_path, eval_input_path)
    # Config
    config_raw_path = f"configs/config_original.cfg"
    config_1_path = f"configs/{params['model-1']['config']}"
    if not os.path.exists(config_1_path ): 
        shutil.copy(config_raw_path, config_1_path)
    config_2_path = f"configs/{params['model-2']['config']}"
    if not os.path.exists(config_2_path): 
        shutil.copy(config_raw_path, config_2_path)

if __name__ == "__main__":
    main()

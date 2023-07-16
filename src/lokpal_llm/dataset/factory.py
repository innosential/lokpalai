from .gpt4_all import TrainGPT4All
from .alpaca import TrainSAD

def load_data(config, tokenizer):
    if config.data_type == "alpaca":
        data = TrainSAD(
            config.dataset,
            config.val_set_size,
            tokenizer,
            config.cutoff_len
        )

    elif config.data_type == "gpt4all":
        data = TrainGPT4All(
            config.dataset,
            config.val_set_size,
            tokenizer,
            config.cutoff_len
        )

    else:
        raise ValueError(f"Invalid data name: {config.data_type}")

    data.prepare_data(use_eos_token=config.use_eos_token)
    return data


DATA_TYPES = [
    "alpaca",
    "gpt4all",
]

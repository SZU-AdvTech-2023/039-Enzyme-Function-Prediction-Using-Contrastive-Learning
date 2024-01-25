# 训练
from CLEAN.utils import *
ensure_dirs("data/esm_data")
ensure_dirs("data/pretrained")
csv_to_fasta("data/split100.csv", "data/split100.fasta")
retrive_esm1b_embedding("split100")

from CLEAN.utils import mutate_single_seq_ECs, retrive_esm1b_embedding
train_file = "split30"
train_fasta_file = mutate_single_seq_ECs(train_file)
retrive_esm1b_embedding(train_fasta_file)

from CLEAN.utils import compute_esm_distance
train_file = "split100"
compute_esm_distance(train_file)


# 推断
from CLEAN.utils import *
csv_to_fasta("data/new.csv", "data/new.fasta")
retrive_esm1b_embedding("new")

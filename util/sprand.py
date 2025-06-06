
import torch
from torch_sparse import SparseTensor, SparseStorage
from typing import Tuple


def sprand(dim: Tuple[int, int], nnz: int) -> SparseTensor:
    nu, nv = dim
    row = torch.randint(nu, (nnz,))
    col = torch.randint(nv, (nnz,))

    storage = SparseStorage(row=row, col=col, sparse_sizes=(nu, nv), is_sorted=False)
    storage = storage.coalesce(reduce="max")

    return SparseTensor.from_storage(storage)

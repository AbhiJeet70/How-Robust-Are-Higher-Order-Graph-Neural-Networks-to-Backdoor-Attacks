# How-Robust-Are-Higher-Order-Graph-Neural-Networks-to-Backdoor-Attacks-

---
This repository contains the implementation and analysis of existing backdoor attacks on Graph Neural Nerworks both traditional (GCN, GAT and GraphSage) and Higher Order Graph Neural Network (ESAn, SUN and SAGN).

**Results on the Cora dataset. Each cell shows ASR_mean±ASR_std / Clean_mean±Clean_std (%). HOGNN values in bold indicate better (lower) ASR or (higher) Accuracy than all Traditional GNNs.**

| Model        | GNN Type      | Baseline                   | SBA-Samp                        | SBA-Gen                         | GTA                              | UGBA                             | DPGBA                            |
|--------------|---------------|----------------------------|---------------------------------|---------------------------------|----------------------------------|----------------------------------|----------------------------------|
| **GCN**      | Traditional   | — / 87.4307±1.2121         | 96.67±5.77 / 86.9994±1.4826     | 96.67±5.77 / 86.4449±1.6772     | 70.00±20.00 / 86.1368±1.3955     | 96.67±5.77 / 85.9519±1.7826     | 96.67±5.77 / 85.8903±1.5391     |
| **GraphSage**| Traditional   | — / 87.5539±1.6670         | 96.67±5.77 / 87.4923±1.8515     | 96.67±5.77 / 87.4307±1.9474     | 86.67±15.28 / 87.3691±1.0672     | 96.67±5.77 / 87.1842±1.3114     | 96.67±5.77 / 87.2458±1.1543     |
| **GAT**      | Traditional   | — / 85.8287±1.9765         | 93.33±11.55 / 85.4590±2.3767    | 90.00±10.00 / 85.4590±2.6935    | 93.33±11.55 / 84.8429±1.6941     | 90.00±10.00 / 85.0277±2.1317    | 90.00±10.00 / 84.9661±2.0361    |
| **SAGN**     | Higher-Order  | — / 85.8903±1.0180         | **0.00±0.00 / 86.1984±0.2824**   | **0.00±0.00 / 85.9519±0.6665**   | **10.00±0.00 / 86.0136±1.0180**  | **10.00±0.00 / 86.9994±0.9118**  | **0.00±0.00 / 85.5206±0.5647**  |
| **SUN**      | Higher-Order  | — / 85.7671±0.6665         | **0.00±0.00 / 85.5206±0.9304**   | **0.00±0.00 / 85.3358±1.2307**   | **16.67±5.77 / 86.0136±0.7696**  | **10.00±0.00 / 86.1984±0.5942**  | **0.00±0.00 / 86.0136±0.9485**  |
| **ESAN**     | Higher-Order  | — / 77.2027±13.6145        | **0.00±0.00 / 72.0887±20.8537**  | **0.00±0.00 / 72.5406±20.6940**  | **20.00±0.00 / 72.0476±20.6648** | **10.00±0.00 / 72.2325±20.9423** | **0.00±0.00 / 72.2325±20.7785** |

**Results on the CiteSeer dataset. Each cell shows ASR_mean±ASR_std / Clean_mean±Clean_std (%). HOGNN values in bold indicate better (lower) ASR or (higher) Accuracy than all Traditional GNNs.**

| Model        | GNN Type      | Baseline                   | SBA-Samp                        | SBA-Gen                         | GTA                                | UGBA                               | DPGBA                              |
|--------------|---------------|----------------------------|---------------------------------|---------------------------------|------------------------------------|------------------------------------|------------------------------------|
| **GCN**      | Traditional   | — / 73.8346±1.1353         | 95.5556±1.9245 / 72.8822±1.7101 | 96.6667±3.3333 / 72.4311±1.9159 | 90.0000±3.3333 / 72.9825±1.2521   | 96.6667±3.3333 / 73.3333±1.1287   | 96.6667±3.3333 / 73.3835±1.1936   |
| **GraphSage**| Traditional   | — / 76.9424±0.5693         | 93.3333±0.0000 / 76.8421±0.9861 | 93.3333±0.0000 / 76.6917±0.6891 | 92.2222±5.0918 / 76.0401±0.8282   | 94.4444±1.9245 / 75.7393±1.5652   | 93.3333±0.0000 / 75.7393±1.5652   |
| **GAT**      | Traditional   | — / 72.9825±2.0025         | 95.5556±3.8490 / 72.6316±2.2756 | 95.5556±3.8490 / 72.8321±2.3602 | 93.3333±3.3333 / 72.7819±0.9391   | 94.4444±5.0918 / 72.6316±1.5628   | 94.4444±1.9245 / 72.7318±1.5433   |
| **SAGN**     | Higher-Order  | — / 75.9900±0.9668         | **1.1111±1.9245 / 75.6391±1.3782** | **0.0000±0.0000 / 76.3910±0.9391** | **3.3333±0.0000 / 76.0902±0.3979** | **3.3333±0.0000 / 76.1404±0.9064** | **3.3333±0.0000 / 76.0902±1.1353** |
| **SUN**      | Higher-Order  | — / 75.2381±1.0562         | **1.1111±1.9245 / 75.1880±1.2309** | **0.0000±0.0000 / 75.2381±1.0878** | **3.3333±0.0000 / 75.2381±1.3972** | **3.3333±0.0000 / 76.1404±1.1287** | **2.2222±1.9245 / 76.3409±0.9668** |
| **ESAN**     | Higher-Order  | — / 60.5180±18.0534        | **1.1111±1.6667 / 58.4294±21.6466** | **0.3704±1.1111 / 58.4127±21.4382** | **0.0000±0.0000 / 58.3793±21.4583** | **3.3333±0.0000 / 58.2957±21.6545** | **1.8519±1.7568 / 58.3626±21.4456** |


# Project Setup and Installation

This project uses a `requirements.txt` file to list all the Python packages (and their specific versions) that the project depends on. Follow the steps below to set up your environment and install the required dependencies.

## Step 1: Open a Terminal or Command Prompt

Navigate to your project directory containing the `requirements.txt` file.

## Step 2: Create and Activate a Virtual Environment

It is a good practice to create a virtual environment so that the packages you install do not interfere with system-wide packages.

### Creating a Virtual Environment

Run the following command to create a virtual environment (using `venv`):

```bash
python -m venv venv
```

### Activating the Virtual Environment

- **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

## Step 3: Install Dependencies Using pip

With your virtual environment activated (or in your global environment), run the following command:

```bash
pip install -r requirements.txt
```

This command tells pip to read the `requirements.txt` file and install all the listed packages.

## Step 4: Verify Installation

To verify that a package is installed correctly, you can run:

```bash
python -c "import torch; print(torch.__version__)"
```

This should print the installed version of PyTorch.

## Using an IDE

If you're using an IDE such as VS Code, you can use its integrated terminal to run these commands.

```
use python main.py to run all the models.
You can also specify the model which you want the results for by writing python main.py model_type (example: sagn or sun or esan or gnn).
```

## Citations 

```bibtex
@inproceedings{dhali2024power,
  title={The Power of Many: Investigating Defense Mechanisms for Resilient Graph Neural Networks},
  author={Dhali, Abhijeet and Dividino, Renata},
  booktitle={2024 IEEE International Conference on Big Data (BigData)},
  pages={3572--3578},
  year={2024},
  organization={IEEE}
}

@inproceedings{bevilacqua2022equivariant,
  title={Equivariant Subgraph Aggregation Networks},
  author={Beatrice Bevilacqua and Fabrizio Frasca and Derek Lim and Balasubramaniam Srinivasan and Chen Cai and Gopinath Balamurugan and Michael M. Bronstein and Haggai Maron},
  booktitle={International Conference on Learning Representations},
  year={2022},
}

@article{frasca2022understanding,
  title={Understanding and extending subgraph gnns by rethinking their symmetries},
  author={Frasca, Fabrizio and Bevilacqua, Beatrice and Bronstein, Michael and Maron, Haggai},
  journal={Advances in Neural Information Processing Systems},
  volume={35},
  pages={31376--31390},
  year={2022}
}

@inproceedings{zeng2023substructure,
  title={Substructure aware graph neural networks},
  author={Zeng, Dingyi and Liu, Wanlong and Chen, Wenyu and Zhou, Li and Zhang, Malu and Qu, Hong},
  booktitle={Proceedings of the AAAI conference on artificial intelligence},
  volume={37},
  number={9},
  pages={11129--11137},
  year={2023}
}

@inproceedings{kipf2017semi,
  title={Semi-Supervised Classification with Graph Convolutional Networks},
  author={Kipf, Thomas N and Welling, Max},
  booktitle={International Conference on Learning Representations},
  year={2017}
}

@inproceedings{velivckovic2018graph,
  title={Graph Attention Networks},
  author={Veli{\v{c}}kovi{\'c}, Petar and Cucurull, Guillem and Casanova, Arantxa and Romero, Adriana and Li{\`o}, Pietro and Bengio, Yoshua},
  booktitle={International Conference on Learning Representations},
  year={2018}
}

@inproceedings{hamilton2017inductive,
  title={Inductive Representation Learning on Large Graphs},
  author={Hamilton, William L and Ying, Rex and Leskovec, Jure},
  booktitle={Advances in Neural Information Processing Systems},
  year={2017}
}


@inproceedings{zhang2021backdoor,
  title={Backdoor attacks to graph neural networks},
  author={Zhang, Zaixi and Jia, Jinyuan and Wang, Binghui and Gong, Neil Zhenqiang},
  booktitle={Proceedings of the 26th ACM Symposium on Access Control Models and Technologies},
  pages={15--26},
  year={2021}
}


@inproceedings{xi2021graph,
  title={Graph backdoor},
  author={Xi, Zhaohan and Pang, Ren and Ji, Shouling and Wang, Ting},
  booktitle={30th USENIX Security Symposium},
  pages={1523--1540},
  year={2021}
}

@inproceedings{dai2023unnoticeable,
  title={Unnoticeable backdoor attacks on graph neural networks},
  author={Dai, Enyan and Lin, Minhua and Zhang, Xiang and Wang, Suhang},
  booktitle={Proceedings of the ACM Web Conference 2023},
  pages={2263--2273},
  year={2023}
}


@inproceedings{zhang2024rethinking,
  title={Rethinking graph backdoor attacks: A distribution-preserving perspective},
  author={Zhang, Zhiwei and Lin, Minhua and Dai, Enyan and Wang, Suhang},
  booktitle={Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  pages={4386--4397},
  year={2024}
}



# framingham_risk

Functions for calculating the Framingham Risk Score (FRS) for 10-year risk


## Installation

Install via pip:

    pip install git+https://github.com/fonnesbeck/framingham_risk.git
    
## Usage

Here are sample calculations using the `frs` function:

```
>>> from frs import frs
>>> frs(gender='F', age=35, bmi=24.3, sbp=122, ht_treat=False, smk=True, dia=False)
0.029352227213368165
>>> X = ['m', 30, 22.5, 125.0, True, True, True]
>>> frs(*X)
0.0838895
```
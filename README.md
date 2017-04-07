# framingham_risk

Functions for calculating the Framingham Risk Score (FRS) for 10-year cardiovascular risk (D’Agostino *et al.* 2008).


## Installation

Install via pip:

    pip install git+https://github.com/fonnesbeck/framingham_risk.git
    
## Usage

Here are sample calculations using the `frs` function:

```python
>>> from frs import frs
>>> frs(gender='F', time=10, age=35, bmi=24.3, sbp=122, ht_treat=False, smk=True, dia=False)
0.029352227213368165
>>> X = ['m', 10, 30, 22.5, 125.0, True, True, True]
>>> frs(*X)
0.0838895
```

## References


1. Ralph B. D’Agostino, Ramachandran S. Vasan, Michael J. Pencina, Philip A. Wolf, Mark Cobain, Joseph M. Massaro and William B. Kannel. **General Cardiovascular Risk Profile for Use in Primary Care**. *Circulation*. 2008;117:743-753, originally published February 11, 2008  https://doi.org/10.1161/CIRCULATIONAHA.107.699579

import numpy as np

BETA_WOMEN = np.array([2.72107, # log age
                        0.51125,          # log BMI
                        2.81291,          # log SBP (not treated)
                        2.88267,          # log SBP (treated)
                        0.61868,          # smoking
                        0.77763,          # diabetes
])

BETA_MEN = np.array([3.11296,
                    0.79277,
                    1.85508,
                    1.92672,
                    0.70953,
                    0.53160
])


S_WOMEN = 0.94833
S_MEN = 0.88431

CONST_WOMEN = 26.0145
CONST_MEN = 23.9388

__all__ = ['frs']

def _calc_frs(X, b, surv, const):
    """
    Simple Non-Laboratory Framingham Risk Score (FRS) Calculation.
    
    Parameters
    ----------
    X : array or list
        Input variables for log-age, log-bmi, log sbp (not treated),
        log sbp (treated), smoking, diabetes
    b : array or list
        Variable coefficients
    surv : float
        Baseline survival
    const : float
        Model intercept
    
    """
    return 1 - surv** np.exp(X.dot(b) - const)
    
def frs(gender, age, bmi, sbp, ht_treat, smk, dia):
    """
    10-year risk for women, calculated using the Simple Non-Laboratory 
    Framingham Risk Score (FRS) Calculation.
    
    Parameters
    ----------
    gender : char
        Gender of subject ('M' or 'F')
    age : numeric
        Age of subject
    bmi : numeric
        BMI of subject
    sbp : numeric
        Systolic blood pressure of subject
    ht_treat : bool or int
        Treatment for hypertension (True or False)
    smk : bool or int
        Subject is smoker
    dia : bool or int
        Subject has diabetes
    """
    ht = bool(ht_treat)
    X = np.array([np.log(age), np.log(bmi), np.log(sbp)*(1-ht), np.log(sbp)*ht, bool(smk), bool(dia)])
    if gender.upper()=='F':
        return _calc_frs(X, BETA_WOMEN, S_WOMEN, CONST_WOMEN)
    elif gender.upper()=='M':
        return _calc_frs(X, BETA_MEN, S_MEN, CONST_MEN)
    else:
        raise ValueError('Gender must be specified as M or F')

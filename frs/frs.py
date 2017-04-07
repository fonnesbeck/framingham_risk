import numpy as np


S_WOMEN = 0.99781, 0.99107, 0.98756, 0.98145, 0.97834, 0.97299, 0.96635, 0.96210, 0.95580, 0.94833

S_MEN = 0.99432, 0.98281, 0.97433, 0.95748, 0.94803, 0.93434, 0.92360, 0.91482, 0.90342, 0.88431

CONST_WOMEN = 26.0145
CONST_MEN = 23.9388

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

'''
Calculate standard errors for coefficients using the confidence intervals of the hazard ratio from 
D'Agostino et al. 2008
'''

_calc_sd = lambda interval: (np.log(interval[1]) - np.log(interval[0])) / 3.92

WOMEN_INTERVALS = ((8.59, 26.87),
(0.98, 2.85),
(8.27, 33.54),
(8.97, 35.57),
(1.53, 2.25),
(1.63, 2.91))

SD_WOMEN = [_calc_sd(i) for i in WOMEN_INTERVALS]

MEN_INTERVALS = ((14.80,  34.16),
(1.25,  3.91),
(3.61, 11.33),
(3.90, 12.08),
(1.75, 2.37),
(1.37, 2.11))

SD_MEN = [_calc_sd(i) for i in MEN_INTERVALS]


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

    return 1 - surv** np.exp(X.dot(b.T) - const)
    
def _get_betas(gender, mc, size=1):
    betas = BETA_MEN if gender=='M' else BETA_WOMEN
    if not mc:
        return betas
    
    sds = SD_MEN if gender=='M' else SD_WOMEN

    return np.random.normal(betas, sds, size=(size, len(betas)))
    
def frs(gender, time, age, bmi, sbp, ht_treat, smk, dia, ci=False, alpha=0.05, mc_samples=1000000):
    """
    10-year risk for women, calculated using the Simple Non-Laboratory 
    Framingham Risk Score (FRS) Calculation.
    
    Optionally returns confidence interval for estimate, using Monte Carlo simulation based on the 
    published confidence intervals for the model coefficients.
    
    Parameters
    ----------
    gender : char
        Gender of subject ('M' or 'F')
    time : int
        Time horizon for risk calculation. Must be between 1 and 10.
    age : numeric
        Age of subject
    bmi : numeric
        BMI of subject
    sbp : numeric
        Systolic blood pressure of subject
    ht_treat : bool
        Treatment for hypertension (True or False)
    smk : bool
        Subject is smoker (True or False)
    dia : bool
        Subject has diabetes (True or False)
    ci : bool
        Flag for returning confidence interval with estimate of risk (Defaults to False)
    alpha : float
        Alpha level for confidence interval calculateion (Defaults to 0.05)
    mc_samples : int
        Number of Monte Carlo samples to use in confidence interval calculation
    
    Returns
    -------
    
    risk : estimate of risk
    
    If `ci=True`, the median risk and 100*(1-alpha)% confidence interval is returned:
    
    median, (lower, upper)
    
    """
    if time<1 or time>10:
        raise ValueError('Risk can only be calculated for 1 to 10 year time horizon')
    
    ht = bool(ht_treat)
    X = np.array([np.log(age), np.log(bmi), np.log(sbp)*(1-ht), np.log(sbp)*ht, bool(smk), bool(dia)])
    
    if gender.upper()=='F':
        risk =  _calc_frs(X, _get_betas('F', ci, mc_samples), S_WOMEN[time-1], CONST_WOMEN)
    elif gender.upper()=='M':
        risk =  _calc_frs(X, _get_betas('M', ci, mc_samples), S_MEN[time-1], CONST_MEN)
    else:
        raise ValueError('Gender must be specified as M or F')
        
    if np.shape(risk):
        lower, median, upper = np.percentile(risk, (100*alpha/2, 50, 100*(1-alpha/2)))
        return median, (lower, upper)
    return risk
    
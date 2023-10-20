import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd


def fuzzy_min(mf, value):
    """
    Returns the result of MIN operator with MF
    """
    return np.minimum(mf, value)


def fuzzy_union(*mfs):
    """
    Returns the Union of MF
    """
    x = np.array(mfs)
    return np.amax(x, axis=0)


def draw_fuzzy_set(x, mf):
    """
    Plots the Fuzzy Set.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r"$\mu$(x)")
    ax.set_xlabel("x")
    ax.set_ylim([0, 1.2])
    ax.plot(x, mf)
    plt.grid(True)
    plt.show()


def draw_fuzzy_term(x, mf, title: str):
    """
    Plots the Fuzzy Term.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r"$\mu$(x)")
    ax.set_xlabel("x")
    ax.set_ylim([0, 1.2])
    ax.plot(x, mf)
    plt.grid(True)
    plt.title(title)
    plt.show()


def draw_fuzzy_area(x, mf):
    """
    Plots the Fuzzy Term.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r"$\mu$(x)")
    ax.set_xlabel("x")
    ax.set_ylim([0, 1.2])
    ax.plot(x, mf)
    ax.fill_between(x, mf)
    plt.grid(True)
    plt.show()


def draw_lvu(lv):
    """
    Plots the Linguistic Variable.
    """
    fig, ax = plt.subplots()
    ax.set_ylabel(r"$\mu$(x)")
    ax.set_xlabel("x")
    ax.set_ylim([0, 1.2])
    for term in lv["terms"]:
        x, mf = lv["U"], lv["terms"][term]
        ax.plot(x, mf, label=term)
        ax.legend()

    plt.grid(True)
    plt.title(lv["name"])
    plt.show()


def draw_lv(lv, f=None):
    """
    Plots the Linguistic Variable.
    """
    data = pd.DataFrame(lv["terms"])
    if f is None:
        pass
    else:
        data["total"] = f
    a = list(data.columns)
    data[lv["name"]] = np.arange(*lv["X"])

    st.line_chart(data, x=lv["name"], y=a)

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List
tickers = ['HADE.JK', 'HDFA.JK', 'HDTX.JK', 'HERO.JK', 'HEXA.JK', 'HITS.JK', 'HMSP.JK', 'HOME.JK', 'HOTL.JK', 'HRUM.JK', 'IATA.JK', 'IBFN.JK', 'IBST.JK', 'ICBP.JK', 'ICON.JK', 'IGAR.JK', 'IIKP.JK', 'IKAI.JK', 'IKBI.JK', 'IMAS.JK', 'IMJS.JK', 'IMPC.JK', 'INAF.JK', 'INAI.JK', 'INCI.JK', 'INCO.JK', 'INDF.JK', 'INDR.JK', 'INDS.JK', 'INDX.JK', 'INDY.JK', 'INKP.JK', 'INPC.JK', 'INPP.JK', 'INRU.JK', 'INTA.JK', 'INTD.JK', 'INTP.JK', 'JIHD.JK', 'JKON.JK', 'JKSW.JK', 'JPFA.JK', 'JRPT.JK', 'JSMR.JK', 'JSPT.JK', 'JTPE.JK', 'KAEF.JK', 'KARW.JK', 'KBLI.JK', 'KBLM.JK', 'KBLV.JK', 'KBRI.JK', 'KDSI.JK', 'KIAS.JK', 'KICI.JK', 'KIJA.JK', 'KKGI.JK', 'KLBF.JK', 'KOBX.JK', 'KOIN.JK', 'KONI.JK', 'KOPI.JK', 'KPIG.JK', 'KRAH.JK', 'KRAS.JK', 'KREN.JK', 'LAPD.JK', 'LCGP.JK', 'LEAD.JK', 'LINK.JK', 'LION.JK', 'LMAS.JK', 'LMPI.JK', 'LMSH.JK', 'LPCK.JK', 'LPGI.JK', 'LPIN.JK', 'LPKR.JK', 'LPLI.JK', 'LPPF.JK', 'LPPS.JK', 'LRNA.JK', 'LSIP.JK', 'LTLS.JK', 'MAGP.JK', 'MAIN.JK', 'MAMI.JK', 'MAPI.JK', 'MASA.JK', 'MAYA.JK', 'MBAP.JK', 'MBSS.JK', 'MBTO.JK', 'MCOR.JK', 'MDIA.JK', 'MDKA.JK', 'MDLN.JK', 'MDRN.JK', 'MEDC.JK', 'MEGA.JK', 'MERK.JK', 'META.JK', 'MFIN.JK', 'MFMI.JK', 'MGNA.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MIRA.JK', 'MITI.JK', 'MKPI.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMLP.JK', 'MNCN.JK', 'MPMX.JK', 'MPPA.JK', 'MRAT.JK', 'MREI.JK', 'MSKY.JK', 'MTDL.JK', 'MTFN.JK', 'MTLA.JK', 'MTSM.JK', 'MYOH.JK', 'MYOR.JK', 'MYRX.JK', 'MYTX.JK', 'NELY.JK', 'NIKL.JK', 'NIPS.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NRCA.JK', 'OCAP.JK', 'OKAS.JK', 'OMRE.JK', 'PADI.JK', 'PALM.JK', 'PANR.JK', 'PANS.JK', 'PBRX.JK', 'PDES.JK', 'PEGE.JK', 'PGAS.JK', 'PGLI.JK', 'PICO.JK', 'PJAA.JK', 'PKPK.JK', 'PLAS.JK', 'PLIN.JK', 'PNBN.JK', 'PNBS.JK', 'PNIN.JK', 'PNLF.JK', 'PNSE.JK', 'POLY.JK', 'POOL.JK', 'PPRO.JK', 'PRAS.JK', 'PSAB.JK', 'PSDN.JK', 'PSKT.JK', 'PTBA.JK', 'PTIS.JK', 'PTPP.JK', 'PTRO.JK', 'PTSN.JK', 'PTSP.JK', 'PUDP.JK', 'PWON.JK', 'PYFA.JK', 'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RDTX.JK', 'RELI.JK', 'RICY.JK', 'RIGS.JK', 'RIMO.JK', 'RODA.JK', 'ROTI.JK', 'RUIS.JK', 'SAFE.JK', 'SAME.JK', 'SCCO.JK', 'SCMA.JK', 'SCPI.JK', 'SDMU.JK', 'SDPC.JK', 'SDRA.JK', 'SGRO.JK', 'SHID.JK', 'SIDO.JK', 'SILO.JK', 'SIMA.JK']


# Remove duplicates
tickers = list(set(tickers))

# Tick rules
def calculate_tick(price):
    if price < 200:
        return 1
    elif 200 <= price < 500:
        return 2
    elif 500 <= price < 2000:
        return 5
    elif 2000 <= price < 5000:
        return 10
    else:
        return 25

# Fetch data
def fetch_data():
    spread_data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.info
        bid, ask = data.get("bid"), data.get("ask")

        if bid and ask:
            spread = ask - bid
            tick = calculate_tick(bid)
            real_spread = spread - (tick * 2)
            spread_percent = (real_spread / bid) * 100 if bid > 0 else 0
            gain_trade = (real_spread / bid) * 100 if bid > 0 else 0

            spread_data.append({
                "Ticker": ticker, 
                "Bid": bid, 
                "Ask": ask, 
                "Spread": spread, 
                "Real Spread": real_spread, 
                "Spread (%)": spread_percent,
                "Gain/Trade (%)": gain_trade
            })
    return pd.DataFrame(spread_data)

# Fetch data initially
df = fetch_data()

# Display data
st.write("### Spread Data with Gain/Trade (%)")
st.dataframe(df)

# Top 3 by Gain/Trade (%)
st.write("### Top 3 Stocks by Gain/Trade (%)")
st.table(df.nlargest(5, "Gain/Trade (%)"))

# Visualization
if not df.empty:
    st.write("### Gain/Trade (%) Visualization")
    fig, ax = plt.subplots()
    df.dropna().plot.bar(x="Ticker", y="Gain/Trade (%)", ax=ax, color="blue", legend=False)
    plt.title("Gain/Trade (%) per Ticker")
    plt.xlabel("Ticker")
    plt.ylabel("Gain/Trade (%)")
    st.pyplot(fig)

# Refresh button
if st.button("Refresh Data"):
    df = fetch_data()
    st.dataframe(df)

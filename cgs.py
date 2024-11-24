import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Stock Spread Analysis")

# Tickers List
tickers = ['MERK.JK', 'META.JK', 'MFIN.JK', 'MFMI.JK', 'MGNA.JK', 'MICE.JK', 'MIDI.JK', 'MIKA.JK', 'MIRA.JK', 'MITI.JK', 'MKPI.JK', 'MLBI.JK', 'MLIA.JK', 'MLPL.JK', 'MLPT.JK', 'MMLP.JK', 'MNCN.JK', 'MPMX.JK', 'MPPA.JK', 'MRAT.JK', 'MREI.JK', 'MSKY.JK', 'MTDL.JK', 'MTFN.JK', 'MTLA.JK', 'MTSM.JK', 'MYOH.JK', 'MYOR.JK', 'MYRX.JK', 'MYTX.JK', 'NELY.JK', 'NIKL.JK', 'NIPS.JK', 'NIRO.JK', 'NISP.JK', 'NOBU.JK', 'NRCA.JK', 'OCAP.JK', 'OKAS.JK', 'OMRE.JK', 'PADI.JK', 'PALM.JK', 'PANR.JK', 'PANS.JK', 'PBRX.JK', 'PDES.JK', 'PEGE.JK', 'PGAS.JK', 'PGLI.JK', 'PICO.JK', 'PJAA.JK', 'PKPK.JK', 'PLAS.JK', 'PLIN.JK', 'PNBN.JK', 'PNBS.JK', 'PNIN.JK', 'PNLF.JK', 'PNSE.JK', 'POLY.JK', 'POOL.JK', 'PPRO.JK', 'PRAS.JK', 'PSAB.JK', 'PSDN.JK', 'PSKT.JK', 'PTBA.JK', 'PTIS.JK', 'PTPP.JK', 'PTRO.JK', 'PTSN.JK', 'PTSP.JK', 'PUDP.JK', 'PWON.JK', 'PYFA.JK', 'RAJA.JK', 'RALS.JK', 'RANC.JK', 'RBMS.JK', 'RDTX.JK', 'RELI.JK', 'RICY.JK', 'RIGS.JK', 'RIMO.JK', 'RODA.JK', 'ROTI.JK', 'RUIS.JK', 'SAFE.JK', 'SAME.JK', 'SCCO.JK', 'SCMA.JK', 'SCPI.JK', 'SDMU.JK', 'SDPC.JK', 'SDRA.JK', 'SGRO.JK', 'SHID.JK', 'SIDO.JK', 'SILO.JK', 'SIMA.JK', 'SIMP.JK', 'SIPD.JK', 'SKBM.JK', 'SKLT.JK', 'SKYB.JK', 'SMAR.JK', 'SMBR.JK', 'SMCB.JK', 'SMDM.JK', 'SMDR.JK', 'SMGR.JK', 'SMMA.JK', 'SMMT.JK', 'SMRA.JK', 'SMRU.JK', 'SMSM.JK', 'SOCI.JK', 'SONA.JK', 'SPMA.JK', 'SQMI.JK', 'SRAJ.JK', 'SRIL.JK', 'SRSN.JK', 'SRTG.JK', 'SSIA.JK', 'SSMS.JK', 'SSTM.JK', 'STAR.JK', 'STTP.JK', 'SUGI.JK', 'SULI.JK', 'SUPR.JK', 'TALF.JK', 'TARA.JK', 'TAXI.JK', 'TBIG.JK', 'TBLA.JK', 'TBMS.JK', 'TCID.JK', 'TELE.JK', 'TFCO.JK', 'TGKA.JK', 'TIFA.JK', 'TINS.JK', 'TIRA.JK', 'TIRT.JK', 'TKIM.JK', 'TLKM.JK', 'TMAS.JK', 'TMPO.JK', 'TOBA.JK', 'TOTL.JK', 'TOTO.JK', 'TOWR.JK', 'TPIA.JK', 'TPMA.JK', 'TRAM.JK', 'TRIL.JK', 'TRIM.JK', 'TRIO.JK', 'TRIS.JK', 'TRST.JK', 'TRUS.JK', 'TSPC.JK', 'ULTJ.JK', 'UNIC.JK', 'UNIT.JK', 'UNSP.JK', 'UNTR.JK', 'UNVR.JK', 'VICO.JK', 'VINS.JK', 'VIVA.JK', 'VOKS.JK', 'VRNA.JK', 'WAPO.JK', 'WEHA.JK', 'WICO.JK', 'WIIM.JK', 'WIKA.JK', 'WINS.JK', 'WOMF.JK', 'WSKT.JK', 'WTON.JK', 'YPAS.JK', 'YULE.JK', 'ZBRA.JK', 'SHIP.JK', 'CASA.JK', 'DAYA.JK', 'DPUM.JK', 'IDPR.JK', 'JGLE.JK', 'KINO.JK', 'MARI.JK', 'MKNT.JK', 'MTRA.JK', 'PRDA.JK', 'BOGA.JK', 'BRIS.JK', 'PORT.JK', 'CARS.JK', 'MINA.JK', 'FORZ.JK', 'CLEO.JK', 'TAMU.JK', 'CSIS.JK', 'TGRA.JK', 'FIRE.JK', 'TOPS.JK', 'KMTR.JK', 'ARMY.JK', 'MAPB.JK', 'WOOD.JK', 'HRTA.JK', 'MABA.JK', 'HOKI.JK', 'MPOW.JK', 'MARK.JK', 'NASA.JK', 'MDKI.JK', 'BELL.JK', 'KIOS.JK', 'GMFI.JK', 'MTWI.JK', 'ZINC.JK', 'MCAS.JK', 'PPRE.JK', 'WEGE.JK', 'PSSI.JK', 'MORA.JK', 'DWGL.JK', 'PBID.JK', 'JMAS.JK', 'CAMP.JK', 'IPCM.JK', 'PCAR.JK', 'LCKM.JK', 'BOSS.JK', 'HELI.JK', 'JSKY.JK', 'INPS.JK', 'GHON.JK', 'TDPM.JK', 'DFAM.JK', 'NICK.JK', 'BTPS.JK', 'SPTO.JK', 'PRIM.JK', 'HEAL.JK', 'TRUK.JK', 'PZZA.JK', 'TUGU.JK', 'MSIN.JK', 'SWAT.JK', 'KPAL.JK', 'TNCA.JK', 'MAPA.JK', 'TCPI.JK', 'IPCC.JK', 'RISE.JK', 'BPTR.JK', 'POLL.JK', 'NFCX.JK', 'MGRO.JK', 'NUSA.JK', 'FILM.JK', 'ANDI.JK', 'LAND.JK', 'MOLI.JK', 'PANI.JK', 'DIGI.JK', 'CITY.JK', 'SAPX.JK', 'KPAS.JK', 'SURE.JK', 'HKMU.JK', 'MPRO.JK', 'DUCK.JK', 'GOOD.JK', 'SKRN.JK', 'YELO.JK', 'CAKK.JK', 'SATU.JK', 'SOSS.JK', 'DEAL.JK', 'POLA.JK', 'DIVA.JK', 'LUCK.JK', 'URBN.JK', 'SOTS.JK', 'ZONE.JK', 'PEHA.JK', 'FOOD.JK', 'BEEF.JK', 'POLI.JK', 'CLAY.JK', 'NATO.JK', 'JAYA.JK', 'COCO.JK']


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

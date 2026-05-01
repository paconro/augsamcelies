#!/usr/bin/env python3
"""
Convierte el Excel Cantos_en_leton.xlsx → songs.json
Uso: python3 generar_songs.py [ruta_al_excel]
"""
import pandas as pd
import json
import sys
import os

EXCEL = sys.argv[1] if len(sys.argv) > 1 else 'Cantos_en_leton.xlsx'

if not os.path.exists(EXCEL):
    print(f'Error: no se encuentra {EXCEL}')
    sys.exit(1)

df = pd.read_excel(EXCEL, sheet_name='Dziesmas')

def clean(val):
    if pd.isna(val): return None
    v = str(val).strip()
    return v if v else None

songs = []
for _, row in df.iterrows():
    audio = clean(row.get('Audio 02')) or clean(row.get('Audio'))
    pagina = clean(row.get('Grāmatas lappuse'))
    if pagina:
        try: pagina = str(int(float(pagina)))
        except: pass

    songs.append({
        'id':        clean(row.get('🔒 Row ID')) or str(len(songs)),
        'lv':        clean(row.get('Letón')) or '',
        'es':        clean(row.get('Español')),
        'it':        clean(row.get('Italiano')),
        'pdf':       clean(row.get('PDF')),
        'biblia':    clean(row.get('Bībele')),
        'tiempo':    clean(row.get('Liturģiskais laiks')),
        'eucaristia':clean(row.get('Euharistijas temati')),
        'liturgia':  clean(row.get('Liturģijas temats')),
        'etapa':     clean(row.get('Etaps')),
        'pagina':    pagina,
        'audio':     audio,
        'foto':      clean(row.get('photo 1')),
        'texto':     clean(row.get('Teksts')),
    })

out = 'songs.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)

print(f'✓ Generado {out} con {len(songs)} canciones')
print(f'  Con audio: {sum(1 for s in songs if s["audio"])}')
print(f'  Con PDF:   {sum(1 for s in songs if s["pdf"])}')

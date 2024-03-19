# Správa repozitářů

- Soukromý repozitář, všichni by měli být pozvaní a měli by mít přístup do obou repozitářů a do projektu 

## Popis 

Pro FE i BE jsou 2 oddělené repozitáře, které jsou propojené do jednoho projektu, který můžeme využívat k plánování a sledování práce. 

### Git rules 

Pro oba repozitáře platí, že máme jednu “svatou” branch, ze které budeme vycházet a bude do ní mergovat pracovní branche 

Jakmile budeme chtít na projektu pracovat, vytvoříme novou branch, kterou pojmenujeme ve formátu:  

- **xlogin/[kod ukolu]** - v případě, že má úkol přiřazen úkol na kanbanu nebo 

- **xlogin/[stručný popis úkolu]** - v případě, že nemáme vytvořený úkol a chceme projekt vylepšit/refaktorovat 

Jakmile jsme hotovi a spokojeni se svou prací a chceme změny mergnout -> vytváříme **Pull Request** (v repozitáři na Githubu)

Když vytváříte PR, tak dejte nějaký smyslplný nadpis, který vystihuje řešitelný problém 

Napiště do description co váš kód dělá a přiložte screenshot, pokud tvoříte UI, aby ostatní měli představu, co bylo přidáno/změněno 

Poté co PR vytvoříte, přiřadíte k němu člověka, který by vám to měl zkontrolovat (kdokoliv, kdo tomu rozumí, může jich být víc) 

Pro možnost mergování je potřeba mít schválení od **minimálně jednoho člověka** - chceme předejít zběsilému mergování a rozbíjení kódu ostatních a budete mít jistotu, že s vašim kódem souhlasí alespoň jeden člověk 

Stavy 

- **PR je schváleno** - můžete mergnout do hlavní větve 

- **Na PR jsou važádány změny** - prosím opravte kód podle komentářů nebo si obhajte vaše řešení 

- **PR obsahuje konflikty** - prosím, vyřešte je 

- **PR je zamítnuto** - to nechceme a snad nenastane 

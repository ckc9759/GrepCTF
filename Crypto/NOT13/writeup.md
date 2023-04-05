### Challenge Name : NOT 13

#### Desc : ROT13 isn't the only substitution cipher out there.

Author - @FusterCluck

FLAG FORMAT: grepCTF{...}

msg.txt 
    PULGY MQDIY HUPUL DMX WYGX, JUBDGJXGXIL WHMQMDJMBA GPMX. YULKM DJGPGLMDSIG, BIPPW TMXWG PIJXID XMBJMHIBX, YM XILQMD TGDXMKIPIY XGPPID, IX JUBAIG XILQMD SIWY SIMD WIAIG. QLUMB IPXLMJMGD PIJXID LMDID, GAGX TWLMID LMDID MBXGLHIY DGH. BIBJ MH XMBJMHIBX MQDIY. XNG RPWA MD MXD BUX WPOWED LUX, MB PUOGL JWDG, OMXN IBHGLDJULGD MBDXGWH UR DQWJGD. RIDJG HMJXIY BIPPW GLWX, XMBJMHIBX XGYQID PGJXID IPXLMJMGD TGP.

### Solution 

Since it is obvious from the description the ROT13 wasn't used. 
We will try to use monoalphabetic substitution to solve the challenge

using this link we can automatically solve a monoalphabetic cipher using frequency analysis
https://www.dcode.fr/monoalphabetic-substitution

we the get the following text are deciphering - 
    LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT. MORVI SCELERISQUE, NULLA BITAE LUCTUS TINCIDUNT, MI TURPIS BESTIVULUM TELLUS, UT CONGUE TURPIS QUAM QUIS AUGUE. PROIN ULTRICIES LUCTUS RISUS, EGET BARIUS RISUS INTERDUM SED. NUNC ID TINCIDUNT IPSUM. THE FLAG IS ITS NOT ALWAYS ROT, IN LOWER CASE, WITH UNDERSCORES INSTEAD OF SPACES. FUSCE DICTUM NULLA ERAT, TINCIDUNT TEMPUS LECTUS ULTRICIES BEL. 

Ignoring the placeholder text and accounting for flag format it is easy to see that the flag is :- 
grepCTF{its_not_always_rot}


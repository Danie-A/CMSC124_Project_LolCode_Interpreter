has_error = False

        # if has_error:
        #     pass
        # else:
        #     has_error = True
        #     error("[SyntaxError] Linebreak expected after statement", current_line)
        # return 
        
reg = {
    "varident": r'^[a-zA-Z][a-zA-Z0-9_]*$',
    "numbr_literal": r'^-?([1-9][0-9]*|0)$',
    "numbar_literal": r'^(-?[0-9]*(\.[0-9]+)?)$',
    "yarn_literal": r'^\"[^\"\']*\"$',
    "troof_literal": r'^(WIN|FAIL)$',
    "type_literal": r'^(NOOB|NUMBR|NUMBAR|YARN|TROOF)$',
    "hai": r'^HAI$',
    "kthxbye": r'^KTHXBYE$',
    "wazzup": r'^WAZZUP$',
    "buhbye": r'^BUHBYE$',
    "btw": r'^BTW$',
    "obtw": r'^OBTW$',
    "tldr": r'^TLDR$',
    "ihasa": r'^I HAS A$',
    "itz": r'^ITZ$',
    "r": r'^R$',
    "sum": r'^SUM OF$',
    "diff": r'^DIFF OF$',
    "produkt": r'^PRODUKT OF$',
    "quoshunt": r'^QUOSHUNT OF$',
    "mod": r'^MOD OF$',
    "biggr": r'^BIGGR OF$',
    "smallr": r'^SMALLR OF$',
    "both": r'^BOTH OF$',
    "either": r'^EITHER OF$',
    "won": r'^WON OF$',
    "not": r'^NOT$',
    "any": r'^ANY OF$',
    "all": r'^ALL OF$',
    "bothsaem": r'^BOTH SAEM$',
    "diffrint": r'^DIFFRINT$',
    "smoosh": r'^SMOOSH$',
    "maek": r'^MAEK$',
    "a": r'^A$',
    "isnowa": r'^IS NOW A$',
    "visible": r'^VISIBLE$',
    "gimmeh": r'^GIMMEH$',
    "orly?": r'^O RLY\?$',
    "yarly": r'^YA RLY$',
    "mebbe": r'^MEBBE$',
    "nowai": r'^NO WAI$',
    "oic": r'^OIC',
    "wtf?": r'^WTF\?$',
    "omg": r'^OMG$',
    "omgwtf": r'^OMGWTF$',
    "iminyr": r'^IM IN YR$',
    "uppin": r'^UPPIN$',
    "nerfin": r'^NERFIN$',
    "yr": r'^YR$',
    "til": r'^TIL$',
    "wile": r'^WILE$',
    "imouttayr": r'^IM OUTTA YR$',
    "howiz": r'^HOW IZ I$',
    "ifusayso": r'^IF U SAY SO$',
    "gtfo": r'^GTFO$',
    "foundyr": r'^FOUND YR$',
    "iiz": r'^I IZ$',
    "mkay": r'^MKAY$',
}

            
            # if for loop
            # for i in reg_keys:
            #     if re.fullmatch(reg[i], token):
            #         items.append([i, token])
            #         break

    # contents = re.sub(r"(?<=\n)\s*OBTW.*TLDR\s*(?=\n)", "", contents, flags=re.DOTALL) # remove comments by deleting OBTW, between them, and TLDR, flags=re.DOTALL to include multiple lines
    # result = re.sub(r"OBTW.*?TLDR", lambda x: '\n' * x.group(0).count('\n'), contents, flags=re.DOTALL)
    # if line has words before OBTW show error
    
    #result = re.sub(r"(?<=\n)\s*OBTW.*TLDR\s*(?=\n)", lambda x: '\n' * x.group(0).count('\n'), contents, flags=re.DOTALL)
    
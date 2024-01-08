HOW IZ I switchInsideFunc YR choice AN YR input
    BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

	choice IS NOW A NUMBR
	choice
	WTF?
		OMG 1
			VISIBLE "Enter birth year: "
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input
			GTFO
		OMG 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			VISIBLE "Tip: " + PRODUKT OF input AN 0.1
			GTFO
		OMG 3
			VISIBLE "Enter width: "
			GIMMEH input
			VISIBLE "Square Area: " + PRODUKT OF input AN input
			GTFO
		OMG 0
			VISIBLE "Goodbye"
		OMGWTF
			VISIBLE "Invalid Input!"
	OIC

    FOUND YR "Switch Working Inside Function"
IF U SAY SO

HOW IZ I ifElseInsideFunc YR choice AN YR input
	BTW if w/o MEBBE, 1 only, everything else is invalid
	VISIBLE "1. Compute age"
	VISIBLE "2. Compute tip"
	VISIBLE "3. Compute square area"
	VISIBLE "0. Exit"

	VISIBLE "Choice: "
	GIMMEH choice

	BOTH SAEM choice AN 1
	O RLY?
		YA RLY
			VISIBLE "Enter birth year: "
			GIMMEH input
			VISIBLE DIFF OF 2022 AN input

	BTW uncomment this portion if you have MEBBE
	BTW else, this portion should be ignored

		MEBBE BOTH SAEM choice AN 2
			VISIBLE "Enter bill cost: "
			GIMMEH input
			VISIBLE "Tip: " PRODUKT OF input AN 0.1
		MEBBE BOTH SAEM choice AN 3
			VISIBLE "Enter width: "
			GIMMEH input
			VISIBLE "Square Area: " PRODUKT OF input AN input
		MEBBE BOTH SAEM choice AN 0
			VISIBLE "Goodbye"

		NO WAI
			VISIBLE "Invalid Input!"
	OIC

	DIFFRINT BIGGR OF 3 AN choice AN 3
	O RLY?
		YA RLY
			VISIBLE "Invalid input is > 3."
	OIC
    FOUND YR "If-Else Working Inside Function"
IF U SAY SO

HAI

    HOW IZ I loopInsideFunc YR num1 AN YR num2
        num2 R 0

        IM IN YR asc UPPIN YR num2 WILE BOTH SAEM num2 AN SMALLR OF num2 AN num1
            VISIBLE num2
        IM OUTTA YR asc

        VISIBLE "***"

        IM IN YR desc NERFIN YR num2 TIL BOTH SAEM num2 AN 0
            VISIBLE num2
        IM OUTTA YR desc
        FOUND YR "Loop Working Inside Function"
    IF U SAY SO

    WAZZUP
        I HAS A ...
        num1
        I HAS A num2
        I HAS A choice
        I HAS A input
    BUHBYE

    GIMMEH num1
    GIMMEH num2

    I IZ loopInsideFunc YR num1 AN YR num2
    VISIBLE IT !
    VISIBLE ...
    "YEHEY!"

    I IZ ifElseInsideFunc YR choice AN YR input
    VISIBLE IT

    I IZ switchInsideFunc YR choice AN YR input
    VISIBLE IT

KTHXBYE
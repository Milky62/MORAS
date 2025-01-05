@32727
D = A;
@6
M = D;	//RAM[6] = 32727 -> najmanja prvotna vrijednost

@0
D = A;
@10
M = D;	// i = 0, koristi RAM[10] za spremanje indeksa petlje	

// Loopanje RAM[0] do RAM[4]
(LOOP_START)
	@10
	D = M; // dohvaca indeks i
	@0
	A = D; // pointa na RAM[i]
	D = M; // ucitava vrijednost na RAM[i]

	@POS_CHECK
	D; JGT 		// ako je vrijednost > 0, skace na POS_CHECK
	@SKIP
	0; JMP 		// inace skip na drugu iteraciju


(POS_CHECK)
	@6
	D = M - D 	// usporedjuje RAM[i] s RAM[6] tj. D = RAM[6] - RAM[i]
	@UPDATE_MIN
	D; JGT		// ako je RAM[i] < RAM[6], azurirati RAM[6]
	@SKIP
	0; JMP		// inace skip

(UPDATE_MIN)
	@10
	D = M; 		// dohvaca RAM[i]
	@0
	A = D;		//pointa na RAM[i]
	D = M;		// D = RAM[i]
	@6
	M = D; 		// RAM[6] = RAM[i]

(SKIP)
	@10
	M = M + 1;	// M++
	@10
	D = M;
	@5
	D = D - A;	//usporedi i, 5
	@LOOP_START
	D; JLT		// ako je i<5, nastaviti loop


@6
D = M; //dohvati najmanju vrijednost
@5
M = D; //spremi ju u RAM[5]


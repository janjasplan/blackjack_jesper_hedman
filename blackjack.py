print ("-" * 100)
print ("-" * 100)
print ("-" * 100)
import random





class Spelet:
    def __init__(self) -> None:

        """ 
            Här skapas en klass med attributen: 
            * En lista med innehåll som motsvarar de 52 korten   
            * Två listor som representerar spelarens och dealerns kort
            * Två räknare för respektives poäng
            * En check för att undvika att en print angående blackjack skrivs ut vid två separata tillfällen   
            
        """
        self.kortleken: list = [2,3,4,5,6,7,8,9,10,"KNEKT","DAM","KUNG","ESS"] * 4                
        self.dealer_hand: list = []
        self.spelare_hand: list = [] 
        self.spelare_poäng = 0
        self.dealer_poäng = 0
        self.spelare_blackjack = False                                                              
        

        
    def blanda_kort(self) -> None:
        """ 
        Här är en metod för att blanda kortleken
        
        """
        random.shuffle(self.kortleken)


    def poäng_räknare(self, hand):
        """
        * Metod för att räkna poäng
        * Metoden itererar över varje element i listan som tilldelats som argument
        * Ser till att räknaren adderas med 10 ifall ett klätt kort påträffas
        * Ifall iterationen går över ett ess så adderas räknaren poäng med 11 och samtidigt så adderas räknaren ess med 1
        * Om ett "vanligt" tal påträffas så adderas räknaren poäng med talet i fråga 

        * Däremot om räknaren poäng överstiger 21 och räknaren ess är högre än 0 så kommer räknaren poäng att subtraheras med 10 och räknaren ess subtraheras med 1. 
          Detta i och med att ess blir värda 1 istället för 10 ifall poängen överstiger 21

        """

        poäng = 0
        ess = 0
        for kort in hand:
            if kort == "KNEKT" or kort == "DAM" or kort == "KUNG":
                poäng += 10
            elif kort == "ESS":
                poäng += 11
                ess += 1
            else:
                poäng += kort
        while poäng > 21 and ess > 0:
            poäng -= 10
            ess -= 1
        return poäng



    def utskrift_hand_poäng(self,hand,poäng,spelare) -> None:
        """
        * En metod för att hantera repetativa utskrifter
        * Argumenten som ska tilldelas är:
          1. Lista med kort hos spelare eller dealer (beroende på vems poängställning som ska skrivas ut)
          2. Attributet som innehåller poängen
          3. En sträng som beskriver vilken aktör det gäller
        
        """

        hand_utskrift: str = "  ".join(map(str,hand))
        print (f"{spelare}ns hela hand är {hand_utskrift}")
        print (f"{spelare}ns totala poäng är {poäng}")
        print ("-" * 100)    



    def första_giv(self) -> None:
        """

        * Jag använder mig av append samt pop funktionerna för att först tilldela dealer och spelare två kort var
        * Poängen tilldelas med hjälp av metoden poäng_räknare
        * Resultaten skrivs ut med metoden utskrift_hand_poäng

        """
        self.dealer_hand.append(self.kortleken.pop())
        self.dealer_hand.append(self.kortleken.pop())
        self.spelare_hand.append(self.kortleken.pop())
        self.spelare_hand.append(self.kortleken.pop())
        self.spelare_poäng = self.poäng_räknare(self.spelare_hand)
        self.dealer_poäng: int = self.poäng_räknare(self.dealer_hand)
        self.utskrift_hand_poäng(self.spelare_hand, self.spelare_poäng, "Spelare")
        self.utskrift_hand_poäng(self.dealer_hand, self.dealer_poäng, "Dealer")
        

    
    def ett_till_kort(self) -> None:
        """
        * En metod för att hantera spelarens val av att ta ett till kort eller inte
        * En while loop initieras som avslutas ifall spelaren väljer att tacka nej till ett till kort
        * Med hjälp av if satser så skrivs lämpliga printar ut och med funktionen return så kommer programmet att återgå till huvudmetoden
        * Vi har samtidigt en kontroll för att se så spelaren matar in ett giltigt svar (ja eller nej)
        
        """
        while True:
            nytt_kort: str = input("Vill du ha ett till kort? (Skriv [ja] för att fortsätta och [nej] för att stanna!): ").lower()
            print ("-" * 100)
            if nytt_kort == "ja":
                self.spelare_hand.append(self.kortleken.pop())
                self.spelare_poäng: int = self.poäng_räknare(self.spelare_hand)

                if self.spelare_poäng > 21:
                    self.utskrift_hand_poäng(self.spelare_hand,self.spelare_poäng,"Spelare")
                    print ("DU HAR FÅTT ÖVER 21 OCH DÄRMED FÖRLORAT!")
                    print ("-" * 100)
                    return
                
                elif self.spelare_poäng == 21:
                    self.utskrift_hand_poäng(self.spelare_hand,self.spelare_poäng,"Spelare")
                    print ("DU HAR FÅTT BLACKJACK! GRATTIS!!")
                    print ("-" * 100)
                    return 
                
                else:
                    self.utskrift_hand_poäng(self.spelare_hand,self.spelare_poäng,"Spelare")

            elif nytt_kort == "nej":
                print (f"Du väljer att stanna med totala poängen {self.spelare_poäng}")
                print ("-" * 100)
                return
            
            else: 
                print ("Ogiltigt svar! Du behöver svara antingen [ja] eller [nej]")                    

            

                
    def dealers_utdelning_av_kort(self) -> None:
        """
        * Metod för att hantera korten dealern ska få efter att spelaren valt att inte ta emot fler kort
        * While loop med if sats som stämmer av ifall dealern ska få fler kort
        * Om dealern inte ska ha ett till kort så skrivs en print ut och med hjälp av return avslutas metoden

        """
        while True:
            if self.dealer_poäng < self.spelare_poäng and self.spelare_poäng < 22 and self.spelare_poäng != 21:
                self.dealer_hand.append(self.kortleken.pop())
                self.dealer_poäng = self.poäng_räknare(self.dealer_hand)
                
                self.utskrift_hand_poäng(self.dealer_hand, self.dealer_poäng, "Dealer")

            elif self.dealer_poäng == self.spelare_poäng:
                print ("ERA POÄNG ÄR LIKA HÖGA! DEALERN VINNER!!")
                print ("-" * 100)
                return
            elif self.dealer_poäng > 21:
                print ("DEALERN FICK ÖVER 21! DU VINNER!")
                print ("-" * 100)
                return
            elif self.dealer_poäng > self.spelare_poäng:
                print ("DEALERN VINNER!")
                print ("-" * 100)
                return


            

    def spelets_runda(self, spelare_namn) -> None:    
        """
        * Huvudmetoden som hanterar själva spelets gång
        * En while loop skapas så spelaren får välja ifall de vill spela eller inte, med hjälp av variabeln omgång håller vi koll på vilken omgång det är
        * Vi anropar metoderna "blanda_kort" samt "första_giv" för att blanda korten samt dela ut de första två korten till dealern och spelaren
        * Vi kontrollerar med if satser ifall vissa förhållanden möts och avslutar iterationen med continue
        * Metoden ett_till_kort anropas för att ge spelaren chans att ta fler kort. Efter detta så kontrollerar vi spelarens poäng och avslutar iterationen ifall kontrollen är True
        * Metoden dealers_utdelning_av_kort anropas för att tilldela kort till dealern
        
        """
        omgång = 0
        while True:
            omgång += 1
            self.spelare_poäng = 0
            self.dealer_poäng = 0
            self.dealer_hand = []
            self.spelare_hand = []
            self.spelare_blackjack = False

            ny_giv: str = input (f"Kul att se dig igen {spelare_namn}! Vill du spela ett parti BLACKJACK? [ja] eller [nej]: ")
            print ("-" * 100)
            print (f"Blackjack omgång {omgång} för {spelare_namn}".center(100,"-"))
            print ("-" * 100)

            if ny_giv == "ja":
                self.blanda_kort()  
                self.första_giv()

                if self.dealer_poäng == 21 and self.spelare_poäng < 21:
                    print ("DEALERN FICK BLACKJACK! DU FÖRLORAR!")
                    print ("-" * 100)
                    continue

                if self.spelare_poäng == 21 and self.dealer_poäng == 21:
                    print (f"Det blev oavgjort!")
                    print ("-" * 100)
                    continue

                elif self.spelare_poäng == 21 and self.dealer_poäng < 21:
                    print ("DU HAR FÅTT BLACKJACK! GRATTIS!")
                    print ("-" * 100)
                    continue

                
                self.ett_till_kort()

                if self.spelare_poäng > 21:
                    continue
                if self.spelare_poäng == 21:
                    continue

                self.dealers_utdelning_av_kort()
            
            elif ny_giv == "nej":
                print ("HEJDÅ!")
                print ("-" * 100)
                break
            else:
                print ("Det är inte ett giltigt svar!") 
                        
                                 
        

                
" Här skapas två instanser av klassen Spelet()"          
spelare1 = Spelet()
spelare2 = Spelet()


""" 
    * En while loop skapas där användaren får välja mellan två olika spelare samt att avsluta det hela
    * Vid val 1 och 2 så kommer en sträng att tilldelas som argument till metoden spelets_runda för att rätt namn ska tilldelas printarna 
 """
while True:
    print("\nVälj spelare att spela med:")
    print("1. Jesper")
    print("2. Edvin")
    print("3. Avsluta")

    val = input("Ange ditt val (1-3): ")
    print ("-" * 100)

    if val == "1":
        spelare1.spelets_runda("Jesper")
    elif val == "2":
        spelare2.spelets_runda("Edvin")
    elif val == "3":
        print("Hejdå!")
        break
    else:
        print("Ogiltigt val, försök igen.")
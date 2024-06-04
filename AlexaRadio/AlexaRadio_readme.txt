
AlexaRadio für alexaRC4shng
---------------------------

Was ist das hier und was kann es:
	Ein Widget für das AlexaRC4shng Plugin von AndreK. 
	Mit dem Widget können Radiosender von dem Dienst TuneIn und Playliste von Spotify abgespielt werden
	Das Radio kann von Hand oder über einen Präsenzmelder gestartet/beendet werden.
	Zeiten wann das Radio vom Präsenzmelder gestartet werden können per UZSU im Widget in der Visu gesperrt werden.
	Es gibt 5 Stationstasten, die über das Widget in der Visu belegt und konfiguriert werden können.
	    (Weitere Sender, falls nötig, können in Listen in den Items konfiguriert werden.)
	Die Senderliste kann über das Widget sortiert, erweitert oder reduziert werden.
	Die Einschaltlautstärke für das automatische Einschalten kann über das Widget in der Visu festgelegt werden.
	Der Sender für das automatische Einschalten kann über das Widget in der Visu festgelegt werden.
	Das Alexa Gerät kann über das Widget in der Visu ausgewählt werden.
	Diverse Design Funktionen können über das Widget in der Visu eingestellt werden.
	Die Lautstärke des Alexa Geräts kann über das Widget in der Visu angepasst werden.
	
Was wird benötigt:
	Benötigt wird das Plugin AlexaRC4shng von AndreK. Das Plugin sollte funktionstüchtig eingerichtet sein.
	Die Struct Datei die in den Ordner smarthome/structs kommt.
	Die Widget Datei, die in den Ordner Smartvisu/dropins/widgets kommt.
	Die Logic Datei, die in den Ordner smarthome/logics kommt.
	Den Aufruf der Logik der unverändert in die smarthome/etc/logic.yaml Datei eingefügt/ergänzt wird.
	logic.yaml:
	-----------
	AlexaRadio:
		filename: ARadio.py
		visu_acl: 'yes'
		watch_item:
		-   '*.AlexaRadio.Praesenzmelder'
		-   '*.AlexaRadio.PlayPause'
		-   '*.AlexaRadio.Station'
		-   '*.AlexaRadio.Sender.speichern'
		-   '*.AlexaRadio.Volume.Setzen'
	
	Das Struct wird in die eigene Item.yaml Konfiguration eingefügt wie z.B.
	    EG:
		    Raum3:
		        Alexa:
		            struct: my.ARadio_struct.AlexaRadioVorlage
					AlexRadio: # Erweiterung für einen Präsenzmelder (Ist kein PM vorhanden, kann das ab hier weggelassen werden)
						Praesenzmelder:
						    knx_listen: X/X/X  # Hier die GA des Präsenzmelder für ein/ausschalten (dpt1/bool)
							
	P.S. Ich würde auch den Pfad "Alexa:" mit übernehmen, da evtl. noch ein AlexaWecker Widget folgt, da kann man dann die Items dazu dort schön einsortieren.

	Und in der Raumseite der eigenen Visu kommt der Widgetaufruf mit dem Item wo das Struct anknüpfen soll: 
	    {{ widget_Radio.Alexa('', 'EG.Raum3.Alexa') }}
		Hier also 'EG.Raum3.Alexa'
		
WICHTIGER HINWEIS:
Die Option "ITEM BESTÄTIGUNG" in dem Smartvisu Setup muss eingeschaltet sein, damit alle Designfunktionen funktionieren.
Man kann bei der Alexa Api nicht zu oft den Status triggern, da sonst der Zugang für eine Weile seitens des Anbieters gesperrt wird. Deshalb werden die Widget Informationen wie z.B. der Titel am Start nach 6 Sekunden (Alexa braucht etwas zu Einschalten) und danach nur alle 20 Sekunden geholt.
Manchmal dauert es also etwas, bis ein Veränderung angezeigt wird. Bei den Stationstasten blinkt der Button dann diese Zeit lang.		

Erklärung der einzelnen Fenster:
Hauptfenster:
    -Play/Pause Button: 	Zeigt an, ob das Radio spielt oder aus ist.
	-Lautstärke Symbol: 	Hier wird angezeigt, ob das Gerät gemutet ist oder nicht.
	-Lautstärke Zahl:		Hier wird die aktuelle Lautstärke angezeigt. Beim Klick auf die Zahl kann die Lautstärke mit +/- in einem Popupfenster geändert werden und mit dem Button an das Gerät gesendet werden. 
	-Logo Sender:			Hier wird das Logo des aktuellen Senders oder ein eigenes Symbol/Icon/Bild, wenn es einer der 5 Stationstasten entspricht, angezeigt.
	-Weiterhin können hier, je nach Einstellungen die 5 Stationstasten, Der Interpret/Titel und einige Zusatzinfos des Senders mit angezeigt werden.

	-Einstellungen:
		- Alexa Gerätename: Hier kann das Alexagerät ausgewählt werden. Die Geräte werden automatisch ermittelt. Es MUSS allerdings mindestens einmal die Logik getriggert werden, da hier die Geräte ermittelt werden. 
		  Also am besten vorher einmal auf Play oder den reload Button neben der Auswahl drücken.
		- Einschaltsender: Hier wird der Sender eingestellt, der beim Einschalten abgespielt werden soll. Die ersten 5 Sender sind die von den 5 Stationstasten.
		  Mit den drei Punkten (Menü) vor dem Auswahlbutton kann mit einem langen Tastendruck, ein Einstellungsmenü zu der Senderliste geöffnet werden.
		  Hier kann man Sender in der Senderliste 
		      - Hinzufügen (Sendernummer UND Sendernme müssen eingetragen sein.)
			  - Sender löschen (Sendernummer ODER Sendername müssen eingetragen sein)
			  - Sender in der Liste verschieben (Sendernummer ODER Sendername müssen eingetragen sein) 
		- Einschaltlautstärke: Hier wird die Lautstärke angegeben, welche beim Einschalten ausgeführt werden soll. Wenn hier "0" steht, wird die Lautstärke beim Einschalten nicht verändert.
		- Kurzwahl Knöpfe anzeigen: Die 5 Stationstasten werden im Hauptfenster angezeigt.
		- Titel anzeigen: Der Titel/Interpret des aktuellen Songs wird im Hauptfenster angezeigt.
		- Zusatzinfo anzeigen: Zusätzliche Infos des Radiosenders werden im Hauptfenster mit angezeigt.
		- Autom. AN sperren: 	Zeitschaltuhr zum Sperren des automatischen einschalten durch den Präsenzmelder. Hier kann für z.B. die Nacht ein autom. Einschalten des Radios verhindert werden.

    - Stationstasten:
		- Einfacher Klick: Der Radiosender, der der Taste zugeordnet ist wird abgespielt. Für ca. 6 Sekunden blinkt der Button, das ist die Zeit, die benötigt wird um neue Infos zu holen.
		- Langer Klick:		Ein Popupfenster öffnet sich mit den Einstellungen zu der Stationstaste. Hier kann man den Sender/Playlist etc. angeben.
		    
			Übersicht Einstellungspopup Stationstasten:
			- TI-Nr / PL-Name: 	Hier wird die TuneIn Sendernummer angegeben. Die kann man im Browser in der Adresszeile sehen und fäng mit einem "s" an, gefolgt von ein paar Zahlen. z.B. "s8954"
								Oder ein Playlistnahmen einer Spotify Playliste - beispielsweise "Andre"
			- Anzeige Name:		Hier wird der Name des Senders angegeben, der dann in der Liste unter Einstellungen angezeigt wird.
			- Logo Version:		Hier können zwei unterschiedliche Methoden (html1 und html2) eingestellt werden wie ein Senderlogo angezeigt wird. 
			                    Nicht jeder Sender kann alles anzeigen aber manche Sender haben verschiedene Logoversionen. 
								Mit dem Klick auf Speichern (Knopf mit Kreis) wird sofort das neue Logo auf der Stationstaste angezeigt.
								Sollte ein Link nicht erreichbar sein, wird automatisch versucht, ob der zweite Link funktioniert und gegebenenfalls benutzt.
								Sollten beide Links nicht erreichbar sein, werden drei Punkte auf dem Button angezeigt.
								Oder als dritte Möglichkeit ein lokales Bild/Icon auf dem Button dargestellt werden. Das Bild muss dann in "dropins/icons/ws" liegen.
			- Lokales Bild: 	Dateiname mit Endung von dem Lokalen Bild in "dropins/icons/ws"
			- Speichern Knopf:	Mit Klick auf diesen Knopf werden die neuen Werte der Stationstaste und der Senderliste zugeordnet.
	

	
	
	
	
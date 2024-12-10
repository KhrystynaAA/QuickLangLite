import sqlite3

# Function to load phrases into the database
def load_phrases():
    phrases = [
        # Banking Phrases
        ('Banking', 'Je voudrais ouvrir un compte bancaire.', 'I would like to open a bank account.'),
        ('Banking', 'Quels documents dois-je fournir pour ouvrir un compte?', 'What documents do I need to open an account?'),
        ('Banking', 'Puis-je ouvrir un compte en tant qu’étudiant?', 'Can I open an account as a student?'),
        ('Banking', 'Quels types de comptes proposez-vous?', 'What types of accounts do you offer?'),
        ('Banking', 'Y a-t-il un solde minimum requis?', 'Is there a minimum balance required?'),
        ('Deposits and Withdrawals', 'Je voudrais déposer de l’argent.', 'I would like to deposit money.'),
        ('Deposits and Withdrawals', 'Comment retirer de l’argent au distributeur automatique?', 'How do I withdraw money from the ATM?'),
        ('Deposits and Withdrawals', 'Puis-je retirer des espèces ici?', 'Can I withdraw cash here?'),
        ('Deposits and Withdrawals', 'Je veux transférer de l’argent sur un autre compte.', 'I want to transfer money to another account.'),
        ('Deposits and Withdrawals', 'Combien de temps dure un virement bancaire?', 'How long does a bank transfer take?'),
        ('Fees and Charges', 'Y a-t-il des frais mensuels pour ce compte?', 'Are there monthly fees for this account?'),
        ('Fees and Charges', 'Quels sont les frais pour les transferts internationaux?', 'What are the charges for international transfers?'),
        ('Fees and Charges', 'Y a-t-il des frais pour retirer de l’argent au distributeur?', 'Is there a fee for withdrawing cash from ATMs?'),
        ('Fees and Charges', 'Comment contester un frais de transaction?', 'How do I dispute a transaction fee?'),
        ('Fees and Charges', 'Y a-t-il des frais de découvert sur ce compte?', 'Are there overdraft fees on this account?'),
        ('Currency Exchange', 'Puis-je changer de devise ici?', 'Can I exchange currency here?'),
        ('Currency Exchange', 'Quel est le taux de change aujourd’hui?', 'What is today’s exchange rate?'),
        ('Currency Exchange', 'Y a-t-il des frais pour changer de devise?', 'Is there a fee for currency exchange?'),
        ('Currency Exchange', 'Acceptez-vous les dépôts en devises étrangères?', 'Do you accept foreign currency deposits?'),
        ('Currency Exchange', 'Combien d’argent puis-je changer en une seule fois?', 'How much cash can I exchange at once?'),
        ('Customer Support', 'J’ai besoin d’aide avec mon compte.', 'I need help with my account.'),
        ('Customer Support', 'Puis-je prendre rendez-vous avec un conseiller bancaire?', 'Can I make an appointment with a banker?'),
        ('Customer Support', 'Y a-t-il un conseiller qui parle anglais?', 'Is there an English-speaking representative?'),
        ('Customer Support', 'Pouvez-vous expliquer cette lettre que j’ai reçue de la banque?', 'Can you explain this letter I received from the bank?'),
        ('Customer Support', 'Comment fermer mon compte?', 'How do I close my account?'),
        # Additional Phrases
        ('At the Bakery', 'Bonjour, je voudrais...', 'Hello, I would like...'),
        ('At the Bakery', 'Une baguette, s’il vous plaît.', 'A baguette, please.'),
        ('At the Bakery', 'Ça coûte combien ?', 'How much does it cost?'),
        ('At the Bakery', 'Merci, bonne journée !', 'Thank you, have a nice day.'),
        ('At the Grocery Store', 'Où puis-je trouver... ?', 'Where can I find...?'),
        ('At the Grocery Store', 'Je voudrais un sac, s’il vous plaît.', 'I would like a bag, please.'),
        ('At the Grocery Store', 'Puis-je payer par carte ?', 'Can I pay by card?'),
        ('At a Restaurant or Café', 'Puis-je voir le menu, s’il vous plaît ?', 'Can I see the menu, please?'),
        ('At a Restaurant or Café', 'Je voudrais commander...', 'I would like to order...'),
        ('At a Restaurant or Café', 'Avez-vous des plats végétariens ?', 'Do you have any vegetarian dishes?'),
        ('At a Restaurant or Café', 'L’addition, s’il vous plaît.', 'The check, please.'),
        ('Asking for Directions', 'Excusez-moi, où se trouve... ?', 'Excuse me, where is...?'),
        ('Asking for Directions', 'Comment puis-je aller à... ?', 'How do I get to...?'),
        ('Asking for Directions', 'C’est loin ?', 'Is it far?'),
        ('At the Bus or Train/Metro Station', 'Quel est le prix d’un billet?', 'How much does a ticket cost?'),
        ('At the Bus or Train/Metro Station', 'Acceptez-vous les cartes de crédit?', 'Do you accept credit cards?'),
        ('At the Bus or Train/Metro Station', 'Est-ce que le bus va jusqu’à l’arrêt …?', 'Does the bus go to the … stop?'),
        ('At the Bus or Train/Metro Station', 'Quand est-ce que cela s’arrêtera?', 'When will this stop?'),
        ('At the Bus or Train/Metro Station', 'Le billet aller simple', 'One-way ticket.'),
        ('At the Bus or Train/Metro Station', 'Le billet aller-retour', 'Round-trip ticket.'),
        ('At the Bus or Train/Metro Station', 'Je voudrais aller à...', 'I would like to go to…'),
        ('At the Bus or Train/Metro Station', 'À quelle heure est le départ/l’arrivée?', 'At what time is the departure/arrival?'),
        ('At the Post Office', 'Je voudrais envoyer une lettre à... (Nom de l’entreprise ou organisation).', 'I want to send a letter to…(Name of company or organization).'),
        ('At the Post Office', 'Où puis-je acheter un timbre correspondant ?', 'Where can I purchase a related stamp?'),
        ('At the Post Office', 'Est-il possible de payer en espèces ? Par carte ?', 'Is it possible to pay in cash? By card?'),
        ('At the Post Office', 'Je voudrais envoyer ce colis à cette adresse, où puis-je l’emballer ?', 'I want to send this parcel to this address; where can I package it?'),
        ('At the Post Office', 'Combien ça coûte ?', 'How much does it cost?'),
        ('In Case of Emergency', 'À l’aide !', 'Help!'),
        ('In Case of Emergency', 'J’ai besoin d’un médecin.', 'I need a doctor.'),
        ('In Case of Emergency', 'Où se trouve l’hôpital le plus proche ?', 'Where is the nearest hospital?')
    ]

    # Connect to the SQLite database
    conn = sqlite3.connect('phrases.db')
    cursor = conn.cursor()

    # Insert each phrase into the database
    for category, phrase, translation in phrases:
        cursor.execute(
            'INSERT INTO phrases (category, phrase, translation) VALUES (?, ?, ?)',
            (category, phrase, translation)
        )

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Data loaded successfully!")

# Main execution
if __name__ == "__main__":
    load_phrases()

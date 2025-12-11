import time
import random
import os
import sys

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

QUESTIONS = [
    {"q": "Who won the FIFA World Cup in 2022?", "options": ["France", "Brazil", "Argentina", "Germany"], "a": "c"},
    {"q": "Which club has won the most Champions League titles?", "options": ["Liverpool", "AC Milan", "Real Madrid", "Barcelona"], "a": "c"},
    {"q": "What is the standard duration of a football match?", "options": ["90 mins", "80 mins", "100 mins", "60 mins"], "a": "a"},
    {"q": "Who is known as 'CR7'?", "options": ["Ronaldo Nazario", "Cristiano Ronaldo", "Ronaldinho", "Rivellino"], "a": "b"},
    {"q": "Which country hosted the 2014 World Cup?", "options": ["South Africa", "Russia", "Brazil", "Qatar"], "a": "c"},
    {"q": "What is the maximum number of players allowed on the pitch per team?", "options": ["10", "11", "12", "9"], "a": "b"},
    {"q": "Who has won the most Ballon d'Or awards?", "options": ["C. Ronaldo", "Zidane", "Messi", "Pelé"], "a": "c"},
    {"q": "Which English club is nicknamed 'The Red Devils'?", "options": ["Liverpool", "Arsenal", "Man Utd", "Nottm Forest"], "a": "c"},
    {"q": "What does VAR stand for?", "options": ["Video Assistant Referee", "Virtual Action Replay", "Video Action Rule", "Very Angry Referee"], "a": "a"},
    {"q": "Which player is famous for the 'Hand of God'?", "options": ["Messi", "Maradona", "Pelé", "Suarez"], "a": "b"},
    {"q": "Where is the 2026 World Cup being hosted?", "options": ["Europe", "South America", "North America", "Asia"], "a": "c"},
    {"q": "Who is the manager of Manchester City (as of 2024)?", "options": ["Klopp", "Arteta", "Guardiola", "Mourinho"], "a": "c"},
    {"q": "Which country has won the most World Cups?", "options": ["Germany", "Italy", "Argentina", "Brazil"], "a": "d"},
    {"q": "What color card results in a sending off?", "options": ["Yellow", "Blue", "Red", "Black"], "a": "c"},
    {"q": "Which position does Manuel Neuer play?", "options": ["Striker", "Midfielder", "Defender", "Goalkeeper"], "a": "d"},
    {"q": "Which stadium is known as 'The Theatre of Dreams'?", "options": ["Anfield", "Old Trafford", "Camp Nou", "Wembley"], "a": "b"},
    {"q": "Who holds the record for most goals in a single Premier League season?", "options": ["Harry Kane", "Erling Haaland", "Mo Salah", "Thierry Henry"], "a": "b"},
    {"q": "Which country won the Euro 2020 (played in 2021)?", "options": ["England", "Spain", "Italy", "Portugal"], "a": "c"},
    {"q": "How many players are on a football team (including substitutes)?", "options": ["11", "18", "23", "25"], "a": "c"},
    {"q": "Which country hosted the first ever World Cup in 1930?", "options": ["Brazil", "Italy", "Uruguay", "England"], "a": "c"},
    {"q": "Who is the all-time leading scorer in the men's international football?", "options": ["Pelé", "Cristiano Ronaldo", "Lionel Messi", "Miroslav Klose"], "a": "b"},
    {"q": "What is the distance from the penalty spot to the goal line?", "options": ["10 yards", "12 yards", "18 yards", "20 yards"], "a": "b"},
    {"q": "Which continent has won the most FIFA World Cups?", "options": ["Europe", "South America", "Africa", "Asia"], "a": "a"},
    {"q": "Which league is often referred to as 'La Liga'?", "options": ["Premier League", "Serie A", "Bundesliga", "Spanish League"], "a": "d"},
    {"q": "Who was the first player to score 100 Premier League goals?", "options": ["Alan Shearer", "Thierry Henry", "Wayne Rooney", "Sergio Agüero"], "a": "a"},
    {"q": "What is the name of the trophy awarded to the winner of the FIFA World Cup?", "options": ["Jules Rimet Trophy", "Golden Boot", "World Cup Trophy", "FIFA Cup"], "a": "c"},
    {"q": "Which country did Zinedine Zidane represent?", "options": ["Brazil", "France", "Portugal", "Algeria"], "a": "b"},
    {"q": "Which city hosts the famous 'El Clásico' match?", "options": ["Madrid and Barcelona", "Manchester and Liverpool", "Milan and Rome", "London and Paris"], "a": "a"},
    {"q": "How often is the FIFA World Cup held?", "options": ["Every 2 years", "Every 3 years", "Every 4 years", "Every 5 years"], "a": "c"},
    {"q": "Which player has won the most Champions League titles as a manager?", "options": ["Pep Guardiola", "Carlo Ancelotti", "Zinedine Zidane", "Alex Ferguson"], "a": "b"},
    {"q": "What is a 'hat-trick' in football?", "options": ["Three assists in a game", "Three goals by one player in a game", "Three saves by a goalkeeper", "Three yellow cards"], "a": "b"},
    {"q": "Which national team is known as 'The Azzurri'?", "options": ["Brazil", "Germany", "Italy", "Argentina"], "a": "c"},
    {"q": "Who is the youngest player to win the FIFA World Cup?", "options": ["Pelé", "Kylian Mbappé", "Ronaldo Nazario", "Messi"], "a": "a"},
    {"q": "Which club does Robert Lewandowski play for (as of 2024)?", "options": ["Bayern Munich", "Borussia Dortmund", "Barcelona", "Real Madrid"], "a": "c"},
    {"q": "In which country was the 'Panenka' penalty technique originated?", "options": ["Brazil", "Germany", "Czechoslovakia", "Netherlands"], "a": "c"},
    {"q": "Which English team is nicknamed 'The Gunners'?", "options": ["Chelsea", "Tottenham Hotspur", "Arsenal", "Manchester United"], "a": "c"},
    {"q": "Who scored the fastest goal in FIFA World Cup history?", "options": ["Hakan Şükür", "Pelé", "Ronaldo", "David Villa"], "a": "a"},
    {"q": "What is the maximum circumference of a football?", "options": ["68 cm", "70 cm", "72 cm", "74 cm"], "a": "b"},
    {"q": "Which country holds the record for the most Olympic gold medals in men's football?", "options": ["Brazil", "Hungary", "Argentina", "Great Britain"], "a": "b"},
    {"q": "Who was the first African player to win the Ballon d'Or?", "options": ["Didier Drogba", "Samuel Eto'o", "George Weah", "Roger Milla"], "a": "c"},
    {"q": "Which club did David Beckham play for when he won the Champions League?", "options": ["Real Madrid", "Manchester United", "LA Galaxy", "AC Milan"], "a": "b"},
    {"q": "What is the common term for a score of 0-0 in football?", "options": ["Nil-nil", "Blank slate", "Even game", "Zero-zero"], "a": "a"},
    {"q": "Which country has never qualified for a FIFA World Cup?", "options": ["India", "New Zealand", "Iceland", "Jamaica"], "a": "a"},
    {"q": "Who invented the sport of football (soccer)?", "options": ["England", "China", "Greece", "Brazil"], "a": "a"},
    {"q": "Which player has scored the most goals in a calendar year?", "options": ["Lionel Messi", "Cristiano Ronaldo", "Pelé", "Gerd Müller"], "a": "a"},
    {"q": "What is the name of the governing body of international football?", "options": ["UEFA", "FIFA", "CONMEBOL", "AFC"], "a": "b"},
    {"q": "Which country won the first European Championship (Euro) in 1960?", "options": ["Spain", "France", "Soviet Union", "Yugoslavia"], "a": "c"},
    {"q": "How many minutes are added for extra time in a standard football match?", "options": ["15 mins", "20 mins", "30 mins", "No fixed time"], "a": "c"},
    {"q": "Which iconic stadium is located in Rio de Janeiro, Brazil?", "options": ["Allianz Arena", "Wembley Stadium", "Maracanã Stadium", "San Siro"], "a": "c"},
    {"q": "Who is known as 'The King' in Brazilian football?", "options": ["Garrincha", "Zico", "Ronaldo", "Pelé"], "a": "d"},
    {"q": "Which club did Steven Gerrard spend most of his career at?", "options": ["Chelsea", "Manchester United", "Liverpool", "Arsenal"], "a": "c"},
    {"q": "What is the maximum number of substitutions allowed in a competitive match (excluding extra time)?", "options": ["3", "4", "5", "6"], "a": "c"},
    {"q": "Which country holds the record for the biggest win in World Cup history?", "options": ["Germany", "Hungary", "Brazil", "Spain"], "a": "b"},
    {"q": "Which major football tournament is held every four years in Europe?", "options": ["Copa América", "Africa Cup of Nations", "UEFA European Championship", "Asian Cup"], "a": "c"},
    {"q": "Who was the first player to break the 100 million euro transfer fee?", "options": ["Cristiano Ronaldo", "Gareth Bale", "Neymar Jr.", "Paul Pogba"], "a": "b"},
    {"q": "Which country is famous for its 'tiki-taka' style of play?", "options": ["Germany", "Italy", "Spain", "Netherlands"], "a": "c"},
    {"q": "What is the diameter of a standard football goalpost?", "options": ["10 cm", "12 cm", "8 cm", "15 cm"], "a": "b"},
    {"q": "Which player holds the record for the most appearances in the Premier League?", "options": ["Ryan Giggs", "Frank Lampard", "Gareth Barry", "James Milner"], "a": "c"}
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{Colors.GREEN}=========================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.YELLOW}     ⚽  PENALTY SHOOTOUT QUIZ  ⚽ {Colors.RESET}")
    print(f"{Colors.GREEN}=========================================={Colors.RESET}")

def show_rules():
    print_header()
    print(f"{Colors.BOLD}GAME RULES:{Colors.RESET}")
    print("1. It's a Penalty Shootout! 5 Shots (Questions) each.")
    print(f"2. Correct Answer = {Colors.GREEN}GOAL (1 Point){Colors.RESET}")
    print(f"3. Answer under 3 seconds = {Colors.BLUE}TOP BINS! (Style Points){Colors.RESET}")
    print(f"4. Wrong Answer = {Colors.RED}MISS/SAVE (0 Points){Colors.RESET}")
    print("5. Most goals wins.")
    print(f"{Colors.GREEN}=========================================={Colors.RESET}\n")
    input(f"{Colors.YELLOW}Press Enter to Toss Coin and Start...{Colors.RESET}")

def get_answer(question_data, penalty_num, player_name):
    print_header()
    print(f"{Colors.BLUE}{player_name} is stepping up for Penalty #{penalty_num}...{Colors.RESET}\n")
    print(f"{Colors.BOLD}Q: {question_data['q']}{Colors.RESET}\n")

    opts = question_data['options']
    labels = ['a', 'b', 'c', 'd']

    for i in range(4):
        print(f"  {Colors.YELLOW}{labels[i].upper()}){Colors.RESET} {opts[i]}")

    print("\n--------------------------------")
    
    start_time = time.time()
    
    while True:
        try:
            choice = input(f"Aim your shot (a/b/c/d): ").lower().strip()
            if choice in labels:
                break
            else:
                print(f"{Colors.RED}Ref says: Invalid input! Please choose a, b, c, or d.{Colors.RESET}")
        except KeyboardInterrupt:
            sys.exit()
            
    end_time = time.time()

    time_taken = end_time - start_time
    return choice, time_taken

def play_single_penalty(player_name, question_data, penalty_num, current_score, current_history):
    choice, duration = get_answer(question_data, penalty_num, player_name)

    correct_lbl = question_data['a']
    score_change = 0
    visual_element = ''

    print("\n" + "." * 30)
    time.sleep(0.5) 

    if choice == correct_lbl:
        if duration <= 3.0: 
            print(f"{Colors.BLUE}{Colors.BOLD}🚀 GOAL!!! TOP BINS!{Colors.RESET}")
            print(f"An absolute screamer in {duration:.2f} seconds!")
            visual_element = f"{Colors.BLUE}O{Colors.RESET}" 
        else:
            print(f"{Colors.GREEN}{Colors.BOLD}⚽ GOAL!{Colors.RESET}")
            print(f"Calm finish into the corner. ({duration:.2f}s)")
            visual_element = f"{Colors.GREEN}o{Colors.RESET}" 
        score_change = 1
    else:
        # Miss
        print(f"{Colors.RED}{Colors.BOLD}❌ MISSED! The keeper saves it!{Colors.RESET}")
        print(f"The correct spot was: {Colors.YELLOW}{correct_lbl.upper()}{Colors.RESET}")
        visual_element = f"{Colors.RED}X{Colors.RESET}"

    time.sleep(2)
    current_history.append(visual_element)
    return current_score + score_change, current_history

def play_innings(player_name, questions, start_penalty_num=1, current_score=0, current_history=None, target_score=None):
    score = current_score
    history = current_history if current_history is not None else []

    print(f"\n{Colors.BOLD}>>> {player_name} is walking to the spot! <<<{Colors.RESET}")
    time.sleep(1.5)

    for i, q_data in enumerate(questions, start_penalty_num):
        score, history = play_single_penalty(player_name, q_data, i, score, history)

        if target_score is not None and score > target_score:
            print_header()
            print(f"\n{Colors.GREEN}{Colors.BOLD}!!! MATCH WON !!!{Colors.RESET}")
            print(f"{player_name} has scored {score} goals, beating the target of {target_score}!")
            print(f"There is no need to take the remaining penalties.")
            time.sleep(6)
            break

    return score, history

def print_row(name, score, hist):
    hist_str = " ".join(hist)
    print(f"{name:15} | {Colors.BOLD}{score}{Colors.RESET} | [{hist_str}]")

def main():
    show_rules()

    p1_name = input("Enter Player 1 Name: ").strip() or "Player 1"
    p2_name = input("Enter Player 2 Name: ").strip() or "Player 2"

    random.shuffle(QUESTIONS)
    if len(QUESTIONS) < 12: 
        print("Error: Not enough questions in database for a full game.")
        return

    p1_initial_questions = QUESTIONS[:5]
    p2_initial_questions = QUESTIONS[5:10]
    
    remaining_questions = QUESTIONS[10:] 

    
    p1_score, p1_hist = play_innings(p1_name, p1_initial_questions)

    print_header()
    print(f"{Colors.YELLOW}HALF TIME REPORT{Colors.RESET}")
    print(f"{p1_name} has set the bar with {Colors.BOLD}{p1_score} goals{Colors.RESET}.")
    print(f"{p2_name} needs {p1_score + 1} to win outright.")
    print("\nSwitching sides...")
    time.sleep(3)


    p2_score, p2_hist = play_innings(p2_name, p2_initial_questions, start_penalty_num=1, current_score=0, current_history=None, target_score=p1_score)

    print_header()
    print(f"{Colors.BOLD}{Colors.YELLOW}FINAL SCORE (Regular Time){Colors.RESET}")
    print(f"--------------------------------")
    print_row(p1_name, p1_score, p1_hist)
    print_row(p2_name, p2_score, p2_hist)
    print(f"--------------------------------\n")
 
    sd_round = 0
    q_idx = 0 
    
    while p1_score == p2_score:
        if q_idx + 2 > len(remaining_questions): 
            print(f"{Colors.RED}Not enough questions left! It's a true draw!{Colors.RESET}")
            break

        sd_round += 1
        print_header()
        print(f"{Colors.BOLD}{Colors.YELLOW}SUDDEN DEATH ROUND {sd_round}{Colors.RESET}")
        print(f"--------------------------------")

        p1_score, p1_hist = play_single_penalty(p1_name, remaining_questions[q_idx], 5 + sd_round, p1_score, p1_hist)
        q_idx += 1
        
        print(f"\n{Colors.BOLD}>>> {p2_name} must match or beat that! <<<{Colors.RESET}")
        time.sleep(1.5)
        p2_score, p2_hist = play_single_penalty(p2_name, remaining_questions[q_idx], 5 + sd_round, p2_score, p2_hist)
        q_idx += 1

        print_header()
        print(f"{Colors.BOLD}{Colors.YELLOW}SUDDEN DEATH SCORE (Round {sd_round}){Colors.RESET}")
        print(f"--------------------------------")
        print_row(p1_name, p1_score, p1_hist)
        print_row(p2_name, p2_score, p2_hist)
        print(f"--------------------------------\n")

        if p1_score > p2_score:
            print(f"{Colors.GREEN}🏆 {p1_name} WINS THE SUDDEN DEATH! 🏆{Colors.RESET}")
            return 
        elif p2_score > p1_score:
            print(f"{Colors.GREEN}🏆 {p2_name} WINS THE SUDDEN DEATH! 🏆{Colors.RESET}")
            return 
        else:
             print(f"{Colors.BLUE}STILL TIED! The tension is rising... Next round!{Colors.RESET}")
             time.sleep(3)

    if p1_score > p2_score:
        print(f"{Colors.GREEN}🏆 {p1_name} WINS THE MATCH! 🏆{Colors.RESET}")
    elif p2_score > p1_score:
        print(f"{Colors.GREEN}🏆 {p2_name} WINS THE MATCH! 🏆{Colors.RESET}")
    else:
        print(f"{Colors.BLUE}🤝 IT'S A DRAW!{Colors.RESET}")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()


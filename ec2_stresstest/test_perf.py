import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

url = 'http://serve-sentiment-env.eba-dqpfwvjj.us-east-2.elasticbeanstalk.com/'

def send_request(data):
    return requests.post(url + 'predict', json=data)

def test_harambe():
    data={'text': """
Harambe, Gorilla Killed at Cincinnati Zoo, 'Had to Pay the Price': Experts
Some experts and activists say the Cincinnati Zoo was right to fatally shoot an endangered gorilla after a toddler fell into the animal's enclosure.

Despite outrage from the public, some experts and activists believe the Cincinnati Zoo was right to fatally shoot an endangered gorilla after a toddler fell into the animal's enclosure.

All accredited zoos, such as Cincinnati's, have protocols in place for when an animal threatens staff or visitors. In this case, the zoo had to decide whether to tranquilize 17-year-old Harambe, a 450-pound western lowland gorilla, or to use greater force, said Ed Hansen, CEO of the American Association of Zoo Keepers.

A lethal shot comes with the risk of accidentally shooting the person you're trying to save, but a tranquilizer dart could have taken up to 30 minutes to work and comes with other risks, Hansen said.

"The tranquilizer possibly could have worked, but the key term there is 'possibly.' And if you were to fire a dart at an animal, he could react violently to the first opportunity that presents itself, and that would have been that small child," Hansen told NBC News. "Unfortunately for the gorilla, the only really positive way to ensure the safety of the child was to dispatch the lethal force."

The Dangerous Animal Response Team first tried to coax Harambe out of the exhibit, according to zoo director Thane Maynard, but the team was only able to cajole the female gorillas away from the three-year-old, who slipped through the railing and plummeted more than 10 feet into the exhibit's moat.

Harambe alternated between gently pawing the boy and dragging him. The team resorted to killing him.

"We stand by our decision," Maynard said. "We'd make the same decision today."                    

Maynard said Monday that the Cincinnati Zoo had received an outpouring of support from colleagues around the world — including famed primatologist Jane Goodall.

On Tuesday, the Jane Goodall Institute published the email Goodall had sent to Maynard, which read in part: "Dear Thane, I feel so sorry for you, having to try to defend something which you may well disapprove of ... it is a devastating loss to the zoo, and to the gorillas."

Critics felt the zoo should have done more before killing Harambe, one of fewer than 175,000 western lowland gorillas worldwide. And many urged authorities to hold the boy's parents criminally responsible: An online petition called "Justice for Harambe" had more than 330,000 signatures Tuesday.                   
"""}
    response = send_request(data)
    
    
def test_mctrump():
    data={'text': """
Trump works the fry station and holds a drive-thru news conference at a Pennsylvania McDonald's

Republican presidential nominee Donald Trump has manned the fry station at a McDonald's in Pennsylvania before staging an impromptu news conference, answering questions from reporters through the drive-thru window

By MICHELLE L. PRICE Associated Press and MARC LEVY Associated Press
October 20, 2024, 8:19 AM

FEASTERVILLE-TREVOSE, Pa. -- FEASTERVILLE-TREVOSE, Pa. (AP) — Republican presidential nominee Donald Trump manned the fry station at a McDonald's in Pennsylvania on Sunday before staging an impromptu news conference, answering questions through the drive-thru window.

As reporters and aides watched, an employee showed Trump how to dunk baskets of fries in oil, salt the fries and put them into boxes using a scoop. Trump, a well-known fan of fast food and a notorious germophobe, expressed amazement that he didn't have to touch the fries with his hands.

“It requires great expertise, actually, to do it right and to do it fast,” Trump said with a grin, putting away his suit jacket and wearing an apron over his shirt and tie.

The visit came as he's tried to counter Democratic nominee Kamala Harris' accounts on the campaign of working at the fast-food chain while in college, an experience that Trump has claimed — without offering evidence — never happened.

A large crowd lined the street outside the restaurant in Feasterville-Trevose, which is part of Bucks County, a key swing voter area north of Philadelphia. The restaurant itself was closed to the public for Trump's visit. The former president later attended an evening town hall in Lancaster and the Pittsburgh Steelers home game against the New York Jets.

After serving bags of takeout to people in the drive-thru lane, Trump leaned out of the window, still wearing the apron, to take questions from the media staged outside. The former president, who has constantly promoted falsehoods about his 2020 election loss, said he would respect the results of next month's vote “if it's a fair election.”

He joked about getting one reporter ice cream and when another asked what message he had for Harris on her 60th birthday on Sunday, Trump said, “I would say, ‘Happy Birthday, Kamala,’” adding, “I think I’ll get her some flowers.”

Trump did not directly answer a question of whether he might support increased minimum wages after seeing McDonald’s employees in action but said, “These people work hard. They’re great.”

He added that “I just saw something … a process that’s beautiful.”

When aides finally urged him to wrap things up so he could hit the road to his next event, Trump offered, “Wasn’t that a strange place to do a news conference?”

Trump has fixated in recent weeks on the summer job Harris said she held in college, working the cash register and making fries at McDonald’s while in college. Trump says the vice president has “lied about working” there, but not offered evidence for claiming that.

Representatives for McDonald’s did not respond to a message about whether the company had employment records for one of its restaurants 40 years ago. But Harris spokesman Joseph Costello said the former president's McDonald's visit “showed exactly what we would see in a second Trump term: exploiting working people for his own personal gain.”

“Trump doesn’t understand what it’s like to work for a living, no matter how many staged photo ops he does, and his entire second term plan is to give himself, his wealthy buddies, and giant corporations another massive tax cut,” Costello said in a statement.

In an interview last month on MSNBC, the vice president pushed back on Trump’s claims, saying she did work at the fast-food chain four decades ago when she was in college.

“Part of the reason I even talk about having worked at McDonald’s is because there are people who work at McDonald’s in our country who are trying to raise a family,” she said. “I worked there as a student.”

Harris also said: “I think part of the difference between me and my opponent includes our perspective on the needs of the American people and what our responsibility, then, is to meet those needs.”

Trump has long spread groundless claims about his opponents based on their personal history, particularly women and racial minorities.

Before he ran for president, Trump was a leading voice of the “birther” conspiracy that baselessly claimed President Barack Obama was from Africa, was not an American citizen and therefore was ineligible to be president. Trump used it to raise his own political profile, demanding to see Obama’s birth certificate and five years after Obama did so, Trump finally admitted that Obama was born in the United States.

During his first run for president, Trump repeated a tabloid’s claims that Texas Sen. Ted Cruz’s father, who was born in Cuba, had links to President John F. Kennedy’s assassin, Lee Harvey Oswald. Cruz and Trump competed for the party’s 2016 nomination.

In January of this year, when Trump was facing Nikki Haley, his former U.N. ambassador, in the Republican primary, he shared on his social media network a post with false claims that Haley’s parents were not citizens when she was born, therefore making her ineligible to be president.

Haley is the South Carolina-born daughter of Indian immigrants, making her automatically a native-born citizen and meeting the constitutional requirement to run for president.

And Trump has continued to promote baseless claims during this campaign. Trump said during his presidential debate with Harris that immigrants who had settled in Springfield, Ohio, were eating residents’ pets — a claim he suggested in an interview Saturday was still true even though he could provide no confirmation.

“It is a fundamental value of my organization that we proudly open our doors to everyone who visits the Feasterville community,” the McDonald’s location’s owner, Derek Giacomantonio, said in a statement. “That’s why I accepted former President Trump’s request to observe the transformative working experience that 1 in 8 Americans have had: a job at McDonald’s.”

Police closed the busy streets around the McDonald’s during Trump's visit. Authorities cordoned off the restaurant as a crowd a couple blocks long gathered, sometimes 10- to 15-deep, across the street straining to catch a glimpse of Trump. Horns honked and music blared as Trump supporters waved flags, held signs and took pictures.

John Waters, of nearby Fairless Hills, had never been to a Trump rally and had hoped to see the former president so close to his house after missing other nearby rallies.

“When I drove up, all the cars, unbelievable, I was like, ‘He’s here’s, he’s coming, he’s definitely coming with this all traffic,’” Waters said.

Trump is especially partial to McDonald's Big Macs and Filet-o-Fish sandwiches. He’s talked often about how he trusts big chains more than smaller restaurants since they have big reputations to maintain, and the former president’s staff often pick up McDonald’s and serve it on his plane.

Jim Worthington, a Trump supporter and fundraiser who owns a nearby athletic complex and chaired Pennsylvania’s delegation to the Republican National Convention, said he arranged Trump’s visit to the locally owned McDonald’s franchise.

The campaign contacted him looking for a McDonald’s in Pennsylvania and Worthington started looking for one. He got in touch with Giacomantonio through a friend and talked the franchise owner through some initial nervousness.

Giacomantonio needed to know that McDonald’s corporate offices would be OK with it, first. Second, he was concerned that being seen as a Trump supporter would hurt his business or a spark boycott, Worthington said.

“He certainly had concerns, but I eased his mind, and talked to him about the benefits,” Worthington said.

___

Associated Press writer Will Weissert in Washington contributed to this report.                                             
"""}
    response = send_request(data)
    
    
def test_george():
    data={'text': """
Dead Bird On Sidewalk Leads Man To Contemplate Own Inevitable Collision With Plate Glass

Published:
October 23, 2024

CHICAGO—Realizing there comes a time when everyone crashes into a window, local man Danny Nagler told reporters Wednesday that a dead bird on the sidewalk had led him to contemplate his own inevitable collision with plate glass. “Seeing this bird’s lifeless body lying here on the pavement, I can’t help but be reminded that someday I too will slam headfirst into a large pane of glass at great speed,” said Nagler, pondering how no living thing on the planet had the power to escape the unavoidable reality of smashing directly into a window display and plummeting to the concrete with a broken neck. “The crazy thing is that I, like this bird, probably won’t even see the plate glass coming. I can try all I want to convince myself that my impact with the side of a modern office building won’t happen, but as this bird found out, it’s no use.” At press time, an inconsolable Nagler reportedly got the call that his sickly grandmother had finally met her pane of plate glass.
"""}
    response = send_request(data)
    
def test_burger_king():
    data={'text': """
Burger King Introduces Foot Lettuce on Their Menu

Published: October 22, 2024

MIAMI, FL—In a move that has left fast food enthusiasts both shocked and intrigued, Burger King has announced the introduction of "Foot Lettuce" to their menu. The new item, which is set to debut nationwide next month, has been described by the company as a "bold and innovative" addition to their lineup of fresh ingredients.

According to Burger King spokesperson, the idea for Foot Lettuce came from a viral internet meme that humorously suggested the possibility of such an item. "We wanted to take something that was a joke and turn it into a reality," the spokesperson said. "Our Foot Lettuce is made from the freshest, highest-quality lettuce, and we think our customers are going to love it."

The announcement has sparked a flurry of reactions on social media, with some users expressing excitement and others expressing skepticism. "I can't believe Burger King is actually doing this," one Twitter user wrote. "This is either going to be amazing or a complete disaster."

Despite the mixed reactions, Burger King remains confident that Foot Lettuce will be a hit. "We believe in taking risks and pushing the boundaries of what fast food can be," the spokesperson said. "We can't wait for our customers to try it."

The new Foot Lettuce will be available at all Burger King locations starting November 1st.
"""}
    response = send_request(data)
    
def time_function(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            return end_time - start_time
        return wrapper
    
def stress_test(n):
    

    harambe_times = []
    mctrump_times = []
    george_times = []
    bk_times = []
    
    timed_test_harambe = time_function(test_harambe)
    timed_test_mctrump = time_function(test_mctrump)
    timed_test_george = time_function(test_george)
    timed_test_burger_king = time_function(test_burger_king)
    for _ in range(n):
        harambe_times.append(timed_test_harambe())
        mctrump_times.append(timed_test_mctrump())
        george_times.append(timed_test_george())
        bk_times.append(timed_test_burger_king())
        
    with open('harambe_times.csv', 'w') as f:
        for time in harambe_times:
            f.write(f"{time}\n")
    
    with open('mctrump_times.csv', 'w') as f:
        for time in mctrump_times:
            f.write(f"{time}\n")
    
    with open('george_times.csv', 'w') as f:
        for time in george_times:
            f.write(f"{time}\n")
    
    with open('bk_times.csv', 'w') as f:
        for time in bk_times:
            f.write(f"{time}\n")    
    

def plot_times():
    harambe_times = pd.read_csv('harambe_times.csv', header=None).squeeze() * 1000
    mctrump_times = pd.read_csv('mctrump_times.csv', header=None).squeeze() * 1000
    george_times = pd.read_csv('george_times.csv', header=None).squeeze() * 1000
    bk_times = pd.read_csv('bk_times.csv', header=None).squeeze() * 1000

    data = [harambe_times , mctrump_times, george_times, bk_times]
    avg_times = [harambe_times.mean(), mctrump_times.mean(), george_times.mean(), bk_times.mean()]
    labels = ['Harambe', 'McTrump', 'George', 'Burger King']
    for i in range(len(labels)):
        labels[i] += f' (Avg: {avg_times[i]:.2f})'
    avg_time = sum(avg_times) / len(avg_times)
    longest_time = max(max(harambe_times), max(mctrump_times), max(george_times), max(bk_times))

    plt.figure(figsize=(10, 6))
    plt.axhline(y=avg_time, color='r', linestyle='--', label=f'Average Time: {avg_time:.2f} ms')
    plt.legend()
    plt.boxplot(data, labels=labels)
    plt.title(f'Function Execution Times.\n Average: {avg_time:.2f} ms\n Longest: {longest_time:.2f} ms')
    plt.ylabel('Time (miliseconds)')
    plt.grid(True)
    plt.savefig('execution_times.png')
    plt.show()
    
    
  

if __name__ == '__main__':
    stress_test(100)
    plot_times()
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()


# schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")
    review_date : Optional[str] = Field(default=None, description="Write down the review_date, if available")


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Reviewed in India on 17 May 2023
Style Name: 7KG (Non Inverter)Verified Purchase
I recently purchased the Samsung 7 kg Fully-Automatic Top Loading Washing Machine (model WA70A4002GS/TL) in the beautiful Imperial Silver color, and I must say it has exceeded my expectations. This washing machine has proven to be a reliable workhorse, simplifying my laundry routine and delivering excellent cleaning performance. Here's my detailed review of this appliance:

Design and Build Quality:
The Imperial Silver color of the machine gives it a sleek and modern appearance, effortlessly blending into any contemporary home decor. The top-loading design is incredibly convenient, allowing easy access to the drum. The build quality is solid, and it feels durable, assuring me that it will withstand regular use for years to come.

Capacity and Efficiency:
With a 7 kg capacity, this washing machine is suitable for small to medium-sized families. It accommodates a decent amount of laundry in a single load, saving both time and energy. The appliance is energy-efficient, and I have noticed a significant reduction in my utility bills since I started using it.

Performance and Cleaning Results:
The washing machine's fully-automatic functionality offers hassle-free operation. The drum's unique design ensures optimal water flow and thorough cleaning of clothes. I've been impressed with the cleaning results so far, as it effectively removes stains and dirt, leaving my clothes fresh and odor-free.

Multiple Wash Programs:
The Samsung WA70A4002GS/TL provides a wide range of wash programs to cater to different fabric types and laundry needs. From gentle cycles for delicate garments to intense cleaning for heavily soiled clothes, there's a program for every situation. The intuitive control panel makes it easy to select the desired program and customize settings as per my preference.

Convenience and Features:
This washing machine is packed with convenient features that enhance the overall user experience. The digital display shows the remaining wash time, allowing me to plan my day accordingly. The machine also offers a delay start option, which enables me to set the wash cycle to start later, fitting my schedule. The built-in lint filter efficiently captures lint and ensures that my clothes come out lint-free.

Quiet Operation:
One standout feature of this washing machine is its quiet operation. Even during high-speed spins, it produces minimal noise, allowing me to carry on with other activities without disturbance.

Conclusion:
In conclusion, the Samsung 7 kg Fully-Automatic Top Loading Washing Machine (WA70A4002GS/TL) in Imperial Silver has proven to be an excellent investment. Its sleek design, reliable performance, and efficient cleaning results make it a reliable workhorse in my laundry room. With its versatile wash programs and convenient features, it caters to all my laundry needs. If you're looking for a top-loading washing machine that combines functionality, durability, and efficiency, I highly recommend considering this Samsung model.

Reviewer: Jason
""")

print(result)
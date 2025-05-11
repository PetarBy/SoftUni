from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    TYPE_OF_INFLUENCER = "StandardInfluencer"
    INITIAL_PAYMENT = 0.45

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.type_of_influencer = StandardInfluencer.TYPE_OF_INFLUENCER

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * StandardInfluencer.INITIAL_PAYMENT
        return payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 1.2
            return int(reached_followers)
        if campaign_type == "LowBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 0.9
            return int(reached_followers)

from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer

class PremiumInfluencer(BaseInfluencer):
    TYPE_OF_INFLUENCER = "PremiumInfluencer"
    INITIAL_PAYMENT = 0.85

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.type_of_influencer = PremiumInfluencer.TYPE_OF_INFLUENCER

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * PremiumInfluencer.INITIAL_PAYMENT
        return payment

    def reached_followers(self, campaign_type: str):
        if campaign_type == "HighBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 1.5
            return int(reached_followers)
        if campaign_type == "LowBudgetCampaign":
            reached_followers = self.followers * self.engagement_rate * 0.8
            return int(reached_followers)


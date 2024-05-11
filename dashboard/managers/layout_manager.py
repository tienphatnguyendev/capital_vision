# from screeninfo import get_monitors
# from pages.constants.config import ConfigLayout


# class LayoutManager:
#     def __init__(self):
#         self.width = ConfigLayout.width
#         self.height = ConfigLayout.height

#         self.world_width = 0
#         self.world_height = 0

#         self.ratio_width = 1
#         self.ratio_height = 1

#         self.init_layout()

#     def init_layout(self):
#         self.world_width = get_monitors()[0].width
#         self.world_height = get_monitors()[0].height

#         self.ratio_width = self.world_width / self.width
#         self.ratio_height = self.world_height / self.height

#     def get_width(self, width):
#         return width * self.ratio_width

#     def get_height(self, height):
#         return height * self.ratio_height


# layout_manager = LayoutManager()

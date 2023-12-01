from playwright.sync_api import Page
import config


class IndexPage:
    _BUTTON_FAV = "//div[@class='style-header-add-favorite-M7nA2']"

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def find_fav(self, page: Page) -> None:
        return page.locator(self._BUTTON_FAV).click()
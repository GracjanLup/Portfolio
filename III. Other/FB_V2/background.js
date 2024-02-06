// background.js
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "analyze-reasoning",
    title: "Analyze reasoning",
    contexts: ["selection"],
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "analyze-reasoning") {
    // Store selected text and current tab ID in local storage
    chrome.storage.local.set({ selectedText: info.selectionText, currentTabId: tab.id });

    // Open the options window
    chrome.windows.create({
      url: chrome.runtime.getURL("analysisOptions.html"),
      type: "popup",
      width: 300,
      height: 200,
    });
  }
});

(function () {
  function initDefocus() {
    var scopes = document.querySelectorAll(".defocus-scope");
    scopes.forEach(function (scope) {
      var items = Array.prototype.slice.call(scope.querySelectorAll(".defocus-item"));
      if (!items.length) return;
      var lastPointer = null;
      var scrollFrame = null;

      function setFocus(target) {
        scope.classList.add("is-defocusing");
        items.forEach(function (item) {
          item.classList.toggle("is-focus", item === target || item.contains(target));
        });
      }

      function clearFocus() {
        scope.classList.remove("is-defocusing");
        items.forEach(function (item) {
          item.classList.remove("is-focus");
        });
      }

      function focusedItemAt(x, y) {
        var scopeRect = scope.getBoundingClientRect();
        if (x < scopeRect.left || x > scopeRect.right || y < scopeRect.top || y > scopeRect.bottom) {
          return null;
        }

        var element = document.elementFromPoint(x, y);
        var direct = element && element.closest ? element.closest(".defocus-item") : null;
        if (direct && scope.contains(direct)) return direct;

        var focused = items.reduce(function (best, item) {
          var rect = item.getBoundingClientRect();
          if (rect.bottom < 0 || rect.top > window.innerHeight) return best;
          var center = rect.top + rect.height / 2;
          var distance = Math.abs(center - y);
          if (!best || distance < best.distance) {
            return { item: item, distance: distance };
          }
          return best;
        }, null);
        return focused ? focused.item : null;
      }

      function updateFocusFromPoint(x, y) {
        var target = focusedItemAt(x, y);
        if (target) {
          setFocus(target);
        } else {
          clearFocus();
        }
      }

      scope.addEventListener("pointermove", function (event) {
        lastPointer = { x: event.clientX, y: event.clientY };
        updateFocusFromPoint(event.clientX, event.clientY);
      });
      scope.addEventListener("pointerdown", function (event) {
        lastPointer = { x: event.clientX, y: event.clientY };
        var target = event.target.closest ? event.target.closest(".defocus-item") : null;
        if (target && scope.contains(target)) {
          setFocus(target);
        } else {
          updateFocusFromPoint(event.clientX, event.clientY);
        }
      });
      scope.addEventListener("pointerleave", function () {
        lastPointer = null;
        clearFocus();
      });
      window.addEventListener("scroll", function () {
        if (!lastPointer || !scope.classList.contains("is-defocusing") || scrollFrame) return;
        scrollFrame = window.requestAnimationFrame(function () {
          scrollFrame = null;
          if (lastPointer && scope.classList.contains("is-defocusing")) {
            updateFocusFromPoint(lastPointer.x, lastPointer.y);
          }
        });
      }, { passive: true });
      window.addEventListener("resize", function () {
        if (lastPointer && scope.classList.contains("is-defocusing")) {
          updateFocusFromPoint(lastPointer.x, lastPointer.y);
        }
      });
      items.forEach(function (item) {
        item.addEventListener("focusin", function () { setFocus(item); });
        item.addEventListener("focusout", clearFocus);
      });
    });
  }

  function initKatex() {
    if (!window.renderMathInElement) return;
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false }
      ],
      throwOnError: false
    });
  }

  function initThemeToggle() {
    var button = document.querySelector("[data-theme-toggle]");
    if (!button) return;
    var icon = button.querySelector(".theme-toggle-icon");
    var storageKey = "astrophysical-discovery-theme";
    var root = document.documentElement;

    function storedTheme() {
      try {
        return window.localStorage.getItem(storageKey);
      } catch (error) {
        return null;
      }
    }

    function saveTheme(theme) {
      try {
        window.localStorage.setItem(storageKey, theme);
      } catch (error) {
        return;
      }
    }

    function giscusTheme(theme) {
      return theme === "dark" ? "dark" : "light";
    }

    function setGiscusTheme(theme) {
      var nextTheme = giscusTheme(theme);
      var script = document.querySelector('script[src="https://giscus.app/client.js"]');
      if (script) script.setAttribute("data-theme", nextTheme);

      var iframe = document.querySelector("iframe.giscus-frame");
      if (!iframe || !iframe.contentWindow) return;
      iframe.contentWindow.postMessage(
        { giscus: { setConfig: { theme: nextTheme } } },
        "https://giscus.app"
      );
    }

    function observeGiscusFrame() {
      var comments = document.querySelector(".comments");
      if (!comments || !window.MutationObserver) return;
      var observer = new MutationObserver(function () {
        if (document.querySelector("iframe.giscus-frame")) {
          setGiscusTheme(root.dataset.theme);
        }
      });
      observer.observe(comments, { childList: true, subtree: true });
    }

    function applyTheme(theme) {
      root.dataset.theme = theme;
      button.setAttribute(
        "aria-label",
        theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
      );
      if (icon) icon.textContent = theme === "dark" ? "☀" : "☾";
      setGiscusTheme(theme);
    }

    observeGiscusFrame();
    applyTheme(storedTheme() === "dark" ? "dark" : "light");
    button.addEventListener("click", function () {
      var nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(nextTheme);
      saveTheme(nextTheme);
    });
  }

  function initSpeedReader() {
    var root = document.querySelector("[data-speed-reader]");
    var source = document.querySelector(".writing-detail .prose");
    var stage = document.querySelector("[data-speed-reader-stage]");
    var glance = document.querySelector("[data-speed-reader-glance]");
    if (!root || !source || !stage || !glance) return;

    var panelToggle = root.querySelector("[data-speed-reader-panel-toggle]");
    var panel = root.querySelector("[data-speed-reader-panel]");
    var enabledInput = root.querySelector("[data-speed-reader-enabled]");
    var options = root.querySelector("[data-speed-reader-options]");
    var wpmInput = root.querySelector("[data-speed-reader-wpm]");
    var wpgInput = root.querySelector("[data-speed-reader-wpg]");
    var highlightInput = root.querySelector("[data-speed-reader-highlight]");
    var fontSizeInput = root.querySelector("[data-speed-reader-font-size]");
    var wpmDecreaseButton = root.querySelector("[data-speed-reader-wpm-decrease]");
    var wpmIncreaseButton = root.querySelector("[data-speed-reader-wpm-increase]");
    var wpgDecreaseButton = root.querySelector("[data-speed-reader-wpg-decrease]");
    var wpgIncreaseButton = root.querySelector("[data-speed-reader-wpg-increase]");
    var fontSizeDecreaseButton = root.querySelector("[data-speed-reader-font-size-decrease]");
    var fontSizeIncreaseButton = root.querySelector("[data-speed-reader-font-size-increase]");
    var wpmOutput = root.querySelector("[data-speed-reader-wpm-value]");
    var wpgOutput = root.querySelector("[data-speed-reader-wpg-value]");
    var fontSizeOutput = root.querySelector("[data-speed-reader-font-size-value]");
    var backButton = root.querySelector("[data-speed-reader-back]");
    var playButton = root.querySelector("[data-speed-reader-play]");
    var pauseButton = root.querySelector("[data-speed-reader-pause]");
    var forwardButton = root.querySelector("[data-speed-reader-forward]");
    var panelToggleIcon = panelToggle.querySelector("span");
    if (
      !panelToggle ||
      !panel ||
      !enabledInput ||
      !options ||
      !wpmInput ||
      !wpgInput ||
      !highlightInput ||
      !fontSizeInput ||
      !wpmDecreaseButton ||
      !wpmIncreaseButton ||
      !wpgDecreaseButton ||
      !wpgIncreaseButton ||
      !fontSizeDecreaseButton ||
      !fontSizeIncreaseButton ||
      !wpmOutput ||
      !wpgOutput ||
      !fontSizeOutput ||
      !backButton ||
      !playButton ||
      !pauseButton ||
      !forwardButton
    ) return;

    var storageKey = "joshuaalbert-speed-reader-v1";
    var timer = null;
    var returnHighlightTimer = null;
    var returnHighlightLayer = null;
    var lastSelectionIndex = null;
    var tokens = collectSpeedReaderTokens(source);
    var tokenIndexesByNode = indexSpeedReaderTokensByNode(tokens);
    var state = {
      panelOpen: false,
      enabled: false,
      playing: true,
      index: 0,
      wpm: 300,
      wpg: 3,
      highlight: true,
      fontSize: 38
    };

    loadSettings();
    addSpeedReaderBlurTargets(source);
    setPanelOpen(false);
    syncControls();
    renderGlance();

    if (!tokens.length) {
      panelToggle.disabled = true;
      enabledInput.disabled = true;
      return;
    }

    panelToggle.addEventListener("pointerdown", rememberSourceSelection, true);
    panelToggle.addEventListener("click", function () {
      setEnabled(!state.enabled);
    });

    document.addEventListener("pointerdown", function (event) {
      if (!state.panelOpen || root.contains(event.target)) return;
      setEnabled(false);
    });

    document.addEventListener("selectionchange", function () {
      rememberSourceSelection();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && state.panelOpen) {
        event.preventDefault();
        setEnabled(false);
        return;
      }
      if (
        !state.enabled ||
        (isTypingTarget(event.target) && !root.contains(event.target)) ||
        event.metaKey ||
        event.ctrlKey ||
        event.altKey
      ) return;
      if (event.key === " " || event.key === "Spacebar") {
        event.preventDefault();
        setPlaying(!state.playing);
      } else if (event.key === "ArrowLeft") {
        event.preventDefault();
        moveSeconds(-30);
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        moveSeconds(30);
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        setWpm(state.wpm + 10);
      } else if (event.key === "ArrowDown") {
        event.preventDefault();
        setWpm(state.wpm - 10);
      } else if (event.key === "," || event.key === "<") {
        event.preventDefault();
        setWpg(state.wpg - 1);
      } else if (event.key === "." || event.key === ">") {
        event.preventDefault();
        setWpg(state.wpg + 1);
      }
    });

    enabledInput.addEventListener("change", function () {
      setEnabled(enabledInput.checked);
    });

    wpmInput.addEventListener("input", function () {
      if (wpmInput.value === "") return;
      setWpm(wpmInput.value);
    });
    wpmInput.addEventListener("change", function () {
      setWpm(wpmInput.value);
    });

    wpgInput.addEventListener("input", function () {
      if (wpgInput.value === "") return;
      setWpg(wpgInput.value);
    });
    wpgInput.addEventListener("change", function () {
      setWpg(wpgInput.value);
    });

    highlightInput.addEventListener("change", function () {
      state.highlight = highlightInput.checked;
      saveSettings();
      renderGlance();
    });

    fontSizeInput.addEventListener("input", function () {
      if (fontSizeInput.value === "") return;
      setFontSize(fontSizeInput.value);
    });
    fontSizeInput.addEventListener("change", function () {
      setFontSize(fontSizeInput.value);
    });

    wpmDecreaseButton.addEventListener("click", function () {
      setWpm(state.wpm - 10);
    });
    wpmIncreaseButton.addEventListener("click", function () {
      setWpm(state.wpm + 10);
    });
    wpgDecreaseButton.addEventListener("click", function () {
      setWpg(state.wpg - 1);
    });
    wpgIncreaseButton.addEventListener("click", function () {
      setWpg(state.wpg + 1);
    });
    fontSizeDecreaseButton.addEventListener("click", function () {
      setFontSize(state.fontSize - 1);
    });
    fontSizeIncreaseButton.addEventListener("click", function () {
      setFontSize(state.fontSize + 1);
    });

    backButton.addEventListener("click", function () {
      moveSeconds(-30);
    });
    forwardButton.addEventListener("click", function () {
      moveSeconds(30);
    });
    playButton.addEventListener("click", function () {
      setPlaying(true);
    });
    pauseButton.addEventListener("click", function () {
      setPlaying(false);
    });

    window.addEventListener("resize", function () {
      if (state.enabled) renderGlance();
    });
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(function () {
        if (state.enabled) renderGlance();
      });
    }

    function setPanelOpen(open) {
      state.panelOpen = open;
      root.classList.toggle("is-open", open);
      panelToggle.setAttribute("aria-expanded", open ? "true" : "false");
      panel.setAttribute("aria-hidden", open ? "false" : "true");
      if ("inert" in panel) panel.inert = !open;
      if (!open && panel.contains(document.activeElement)) {
        panelToggle.focus();
      }
    }

    function setEnabled(enabled) {
      var returnIndex = state.index;
      state.enabled = enabled;
      if (enabled) {
        clearReturnHighlight();
        setIndexFromSelection();
        state.playing = true;
      } else {
        clearTimer();
      }
      setPanelOpen(enabled);
      syncControls();
      renderGlance();
      scheduleNext();
      if (!enabled) {
        returnToSourceGlance(returnIndex);
      }
    }

    function setPlaying(playing) {
      if (!state.enabled) return;
      if (playing && state.index >= maxStartIndex() && maxStartIndex() > 0) {
        state.index = 0;
      }
      state.playing = playing;
      syncControls();
      scheduleNext();
    }

    function setWpm(value) {
      state.wpm = clampNumber(value, 0, 1000, state.wpm);
      saveSettings();
      syncControls();
      renderGlance();
      scheduleNext();
    }

    function setWpg(value) {
      state.wpg = clampNumber(value, 1, 15, state.wpg);
      state.index = clampStartIndex(state.index);
      saveSettings();
      syncControls();
      renderGlance();
      scheduleNext();
    }

    function setFontSize(value) {
      state.fontSize = clampNumber(value, 18, 72, state.fontSize);
      saveSettings();
      syncControls();
      renderGlance();
    }

    function moveSeconds(seconds) {
      if (!state.enabled || state.wpm <= 0) return;
      var secondsPerGlance = (60 * state.wpg) / state.wpm;
      var glanceDelta = Math.round(seconds / secondsPerGlance);
      if (glanceDelta === 0 && seconds !== 0) {
        glanceDelta = seconds > 0 ? 1 : -1;
      }
      moveGlances(glanceDelta);
    }

    function moveGlances(glances) {
      state.index = clampStartIndex(state.index + glances * state.wpg);
      renderGlance();
      scheduleNext();
    }

    function renderGlance() {
      document.body.classList.toggle("speed-reading-active", state.enabled);
      stage.hidden = !state.enabled;
      stage.style.setProperty("--speed-reader-font-size", state.fontSize + "px");
      if (!state.enabled) {
        glance.textContent = "";
        return;
      }

      state.index = clampStartIndex(state.index);
      renderGlanceText(tokens.slice(state.index, state.index + state.wpg).map(function (token) {
        return token.text;
      }));
      alignGlance();
    }

    function renderGlanceText(glanceWords) {
      var text = glanceWords.join(" ");
      var characters = Array.from(text);
      var pivotIndex = medianNonWhitespaceIndex(characters);
      glance.textContent = "";
      if (pivotIndex < 0) return;
      var layout = buildGlanceLayout(characters, pivotIndex);
      layout.beforeLines.forEach(function (lineText) {
        appendGlanceLine(lineText, false);
      });
      appendGlancePivotLine(layout.beforePivot, characters[pivotIndex], layout.afterPivot);
      layout.afterLines.forEach(function (lineText) {
        appendGlanceLine(lineText, false);
      });
    }

    function alignGlance() {
      var pivot = glance.querySelector(".speed-reader-pivot");
      var pivotLine = glance.querySelector(".speed-reader-line-pivot .speed-reader-line-inner");
      if (!pivot) return;
      glance.style.setProperty("--speed-reader-y", "0px");
      if (pivotLine) pivotLine.style.setProperty("--speed-reader-line-x", "0px");
      var rect = pivot.getBoundingClientRect();
      var deltaX = window.innerWidth / 2 - (rect.left + rect.width / 2);
      var deltaY = window.innerHeight / 2 - (rect.top + rect.height / 2);
      if (pivotLine) pivotLine.style.setProperty("--speed-reader-line-x", deltaX + "px");
      glance.style.setProperty("--speed-reader-y", deltaY + "px");
    }

    function appendGlanceLine(lineText) {
      if (!lineText.trim()) return;
      var line = document.createElement("div");
      var inner = document.createElement("span");
      line.className = "speed-reader-line";
      inner.className = "speed-reader-line-inner";
      inner.textContent = lineText.trim();
      line.appendChild(inner);
      glance.appendChild(line);
    }

    function appendGlancePivotLine(beforeText, pivotText, afterText) {
      var line = document.createElement("div");
      var inner = document.createElement("span");
      var before = document.createElement("span");
      var pivot = document.createElement("span");
      var after = document.createElement("span");
      line.className = "speed-reader-line speed-reader-line-pivot";
      inner.className = "speed-reader-line-inner";
      before.textContent = beforeText;
      pivot.className = state.highlight ? "speed-reader-pivot is-highlighted" : "speed-reader-pivot";
      pivot.textContent = pivotText;
      after.textContent = afterText;
      inner.appendChild(before);
      inner.appendChild(pivot);
      inner.appendChild(after);
      line.appendChild(inner);
      glance.appendChild(line);
    }

    function buildGlanceLayout(characters, pivotIndex) {
      var pivotWidth = measureGlanceText(characters[pivotIndex]);
      var sideLimit = window.innerWidth * 0.45 - pivotWidth / 2;
      var start = wordStartAt(characters, pivotIndex);
      var end = wordEndAt(characters, pivotIndex);
      var canExpand = true;

      while (canExpand) {
        canExpand = false;
        var leftWidth = measureGlanceText(characters.slice(start, pivotIndex).join(""));
        var rightWidth = measureGlanceText(characters.slice(pivotIndex + 1, end).join(""));
        var leftFirst = leftWidth <= rightWidth;
        if (leftFirst) {
          canExpand = expandLeft() || expandRight();
        } else {
          canExpand = expandRight() || expandLeft();
        }
      }

      return {
        beforeLines: wrapGlanceText(characters.slice(0, start).join("").trim()),
        beforePivot: characters.slice(start, pivotIndex).join(""),
        afterPivot: characters.slice(pivotIndex + 1, end).join(""),
        afterLines: wrapGlanceText(characters.slice(end).join("").trim())
      };

      function expandLeft() {
        var candidateStart = previousWordStart(characters, start);
        if (candidateStart === start) return false;
        var candidateWidth = measureGlanceText(characters.slice(candidateStart, pivotIndex).join(""));
        if (candidateWidth > sideLimit) return false;
        start = candidateStart;
        return true;
      }

      function expandRight() {
        var candidateEnd = nextWordEnd(characters, end);
        if (candidateEnd === end) return false;
        var candidateWidth = measureGlanceText(characters.slice(pivotIndex + 1, candidateEnd).join(""));
        if (candidateWidth > sideLimit) return false;
        end = candidateEnd;
        return true;
      }
    }

    function wrapGlanceText(text) {
      if (!text) return [];
      var maxWidth = window.innerWidth * 0.9;
      var chunks = text.match(/\S+\s*/g) || [];
      var lines = [];
      var line = "";
      chunks.forEach(function (chunk) {
        var candidate = line + chunk;
        if (line && measureGlanceText(candidate.trim()) > maxWidth) {
          lines.push(line.trim());
          line = chunk.trimStart();
        } else {
          line = candidate;
        }
      });
      if (line.trim()) lines.push(line.trim());
      return lines;
    }

    function measureGlanceText(text) {
      if (!measureGlanceText.context) {
        measureGlanceText.context = document.createElement("canvas").getContext("2d");
      }
      var style = window.getComputedStyle(glance);
      measureGlanceText.context.font = [
        style.fontStyle,
        style.fontVariant,
        style.fontWeight,
        style.fontSize,
        style.fontFamily
      ].join(" ");
      return measureGlanceText.context.measureText(text).width;
    }

    function wordStartAt(characters, index) {
      var start = index;
      while (start > 0 && !/\s/.test(characters[start - 1])) start -= 1;
      return start;
    }

    function wordEndAt(characters, index) {
      var end = index + 1;
      while (end < characters.length && !/\s/.test(characters[end])) end += 1;
      return end;
    }

    function previousWordStart(characters, start) {
      var index = start - 1;
      while (index >= 0 && /\s/.test(characters[index])) index -= 1;
      while (index >= 0 && !/\s/.test(characters[index])) index -= 1;
      return Math.max(0, index + 1);
    }

    function nextWordEnd(characters, end) {
      var index = end;
      while (index < characters.length && /\s/.test(characters[index])) index += 1;
      while (index < characters.length && !/\s/.test(characters[index])) index += 1;
      return index;
    }

    function scheduleNext() {
      clearTimer();
      if (!state.enabled || !state.playing || state.wpm <= 0 || !tokens.length) return;
      if (state.index >= maxStartIndex()) {
        state.playing = false;
        syncControls();
        return;
      }
      timer = window.setTimeout(function () {
        moveGlances(1);
      }, (60 * state.wpg * 1000) / state.wpm);
    }

    function clearTimer() {
      if (timer) {
        window.clearTimeout(timer);
        timer = null;
      }
    }

    function syncControls() {
      enabledInput.checked = state.enabled;
      options.disabled = !state.enabled;
      wpmInput.value = state.wpm;
      wpgInput.value = state.wpg;
      highlightInput.checked = state.highlight;
      fontSizeInput.value = state.fontSize;
      wpmOutput.textContent = state.wpm;
      wpgOutput.textContent = state.wpg;
      fontSizeOutput.textContent = state.fontSize;
      playButton.setAttribute("aria-pressed", state.enabled && state.playing ? "true" : "false");
      pauseButton.setAttribute("aria-pressed", state.enabled && !state.playing ? "true" : "false");
      if (panelToggleIcon) panelToggleIcon.textContent = state.enabled ? "X" : "A";
      panelToggle.setAttribute(
        "aria-label",
        state.enabled ? "Turn off speed reading" : "Turn on speed reading"
      );
    }

    function loadSettings() {
      var settings = null;
      try {
        settings = JSON.parse(window.localStorage.getItem(storageKey) || "null");
      } catch (error) {
        settings = null;
      }
      if (!settings) return;
      state.wpm = clampNumber(settings.wpm, 0, 1000, state.wpm);
      state.wpg = clampNumber(settings.wpg, 1, 15, state.wpg);
      state.highlight = typeof settings.highlight === "boolean" ? settings.highlight : state.highlight;
      state.fontSize = clampNumber(settings.fontSize, 18, 72, state.fontSize);
    }

    function saveSettings() {
      try {
        window.localStorage.setItem(storageKey, JSON.stringify({
          wpm: state.wpm,
          wpg: state.wpg,
          highlight: state.highlight,
          fontSize: state.fontSize
        }));
      } catch (error) {
        return;
      }
    }

    function maxStartIndex() {
      if (!tokens.length) return 0;
      return tokens.length - 1;
    }

    function clampStartIndex(value) {
      return Math.min(Math.max(0, Math.floor(value)), maxStartIndex());
    }

    function setIndexFromSelection() {
      rememberSourceSelection();
      var selectedIndex = lastSelectionIndex;
      lastSelectionIndex = null;
      if (selectedIndex === null) return;
      state.index = selectedIndex;
      var selection = window.getSelection ? window.getSelection() : null;
      if (selection) selection.removeAllRanges();
    }

    function getSourceSelectionRange() {
      var selection = window.getSelection ? window.getSelection() : null;
      if (!selection || selection.rangeCount === 0 || selection.isCollapsed) return null;
      var range = selection.getRangeAt(0);
      if (!nodeInsideSource(range.startContainer) || !nodeInsideSource(range.endContainer)) return null;
      return range;
    }

    function rememberSourceSelection() {
      var range = getSourceSelectionRange();
      if (!range) return;
      var selectedIndex = firstTokenIndexInRange(range);
      if (selectedIndex !== null) lastSelectionIndex = selectedIndex;
    }

    function nodeInsideSource(node) {
      if (!node) return false;
      if (node === source) return true;
      var element = node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement;
      return !!element && source.contains(element);
    }

    function firstTokenIndexInRange(range) {
      var startIndex = firstTokenIndexFromRangeStart(range);
      for (var index = startIndex || 0; index < tokens.length; index += 1) {
        if (rangeIntersectsToken(range, tokens[index])) return index;
      }
      return null;
    }

    function firstTokenIndexFromRangeStart(range) {
      if (range.startContainer.nodeType !== Node.TEXT_NODE) return null;
      var indexes = tokenIndexesByNode.get(range.startContainer);
      if (!indexes || !indexes.length) return null;
      for (var offsetIndex = 0; offsetIndex < indexes.length; offsetIndex += 1) {
        if (tokens[indexes[offsetIndex]].end > range.startOffset) {
          return indexes[offsetIndex];
        }
      }
      return Math.min(indexes[indexes.length - 1] + 1, maxStartIndex());
    }

    function returnToSourceGlance(startIndex) {
      var range = rangeForTokenWindow(startIndex, state.wpg);
      if (!range) return;
      var rect = unionRangeRect(range);
      if (!rect) return;
      var targetTop = window.scrollY + rect.top + rect.height / 2 - window.innerHeight / 2;
      window.scrollTo({
        top: Math.max(0, targetTop),
        left: window.scrollX,
        behavior: "auto"
      });
      window.requestAnimationFrame(function () {
        drawReturnHighlight(range);
      });
    }

    function rangeForTokenWindow(startIndex, count) {
      var start = clampStartIndex(startIndex);
      var end = Math.min(tokens.length - 1, start + count - 1);
      var first = tokens[start];
      var last = tokens[end];
      if (!first || !last) return null;
      var range = document.createRange();
      range.setStart(first.node, first.start);
      range.setEnd(last.node, last.end);
      return range;
    }

    function unionRangeRect(range) {
      var rects = Array.prototype.slice.call(range.getClientRects()).filter(function (rect) {
        return rect.width > 0 && rect.height > 0;
      });
      if (!rects.length) return null;
      return rects.reduce(function (union, rect) {
        var left = Math.min(union.left, rect.left);
        var top = Math.min(union.top, rect.top);
        var right = Math.max(union.right, rect.right);
        var bottom = Math.max(union.bottom, rect.bottom);
        return {
          left: left,
          top: top,
          right: right,
          bottom: bottom,
          width: right - left,
          height: bottom - top
        };
      }, rects[0]);
    }

    function drawReturnHighlight(range) {
      clearReturnHighlight();
      returnHighlightLayer = document.createElement("div");
      returnHighlightLayer.className = "speed-reader-return-highlights";
      Array.prototype.slice.call(range.getClientRects()).forEach(function (rect) {
        if (rect.width <= 0 || rect.height <= 0) return;
        var marker = document.createElement("span");
        marker.className = "speed-reader-return-highlight";
        marker.style.left = (window.scrollX + rect.left) + "px";
        marker.style.top = (window.scrollY + rect.top) + "px";
        marker.style.width = rect.width + "px";
        marker.style.height = rect.height + "px";
        returnHighlightLayer.appendChild(marker);
      });
      if (!returnHighlightLayer.children.length) return;
      document.body.appendChild(returnHighlightLayer);
      returnHighlightTimer = window.setTimeout(clearReturnHighlight, 3200);
    }

    function clearReturnHighlight() {
      if (returnHighlightTimer) {
        window.clearTimeout(returnHighlightTimer);
        returnHighlightTimer = null;
      }
      if (returnHighlightLayer) {
        returnHighlightLayer.remove();
        returnHighlightLayer = null;
      }
    }

  }

  function collectSpeedReaderTokens(source) {
    var tokens = [];
    var walker = document.createTreeWalker(source, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var parent = node.parentElement;
        if (!parent || !node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        if (parent.closest("script, style, textarea, input, button")) return NodeFilter.FILTER_REJECT;
        if (parent.closest(".katex-mathml, math, semantics, annotation")) return NodeFilter.FILTER_REJECT;
        if (!parent.closest("h2, h3, h4, h5, h6, p, li, blockquote, figcaption")) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var node = walker.nextNode();
    while (node) {
      var pattern = /\S+/g;
      var match = pattern.exec(node.nodeValue);
      while (match) {
        tokens.push({
          text: match[0],
          node: node,
          start: match.index,
          end: match.index + match[0].length
        });
        match = pattern.exec(node.nodeValue);
      }
      node = walker.nextNode();
    }
    return tokens;
  }

  function indexSpeedReaderTokensByNode(tokens) {
    var indexesByNode = new Map();
    tokens.forEach(function (token, index) {
      var indexes = indexesByNode.get(token.node);
      if (!indexes) {
        indexes = [];
        indexesByNode.set(token.node, indexes);
      }
      indexes.push(index);
    });
    return indexesByNode;
  }

  function addSpeedReaderBlurTargets(source) {
    var header = document.querySelector(".writing-header");
    var comments = document.querySelector(".comments");
    if (header) header.classList.add("speed-reader-blur-target");
    if (comments) comments.classList.add("speed-reader-blur-target");
    Array.prototype.slice.call(
      source.querySelectorAll("h2, h3, h4, h5, h6, p, li, blockquote, pre, table")
    ).forEach(function (element) {
      if (element.querySelector("img, picture, video, canvas")) return;
      element.classList.add("speed-reader-blur-target");
    });
  }

  function medianNonWhitespaceIndex(characters) {
    var indexes = [];
    characters.forEach(function (character, index) {
      if (!/\s/.test(character)) indexes.push(index);
    });
    if (!indexes.length) return -1;
    return indexes[Math.floor((indexes.length - 1) / 2)];
  }

  function rangeIntersectsToken(range, token) {
    try {
      return (
        range.comparePoint(token.node, token.end) >= 0 &&
        range.comparePoint(token.node, token.start) <= 0
      );
    } catch (error) {
      return false;
    }
  }

  function clampNumber(value, min, max, fallback) {
    var number = parseInt(value, 10);
    if (Number.isNaN(number)) return fallback;
    return Math.min(max, Math.max(min, number));
  }

  function isTypingTarget(target) {
    var tagName = target && target.tagName ? target.tagName.toLowerCase() : "";
    return tagName === "input" || tagName === "textarea" || tagName === "select" || target.isContentEditable;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      initDefocus();
      initKatex();
      initThemeToggle();
      initSpeedReader();
    });
  } else {
    initDefocus();
    initKatex();
    initThemeToggle();
    initSpeedReader();
  }
})();

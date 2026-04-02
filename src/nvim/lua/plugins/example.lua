return {
  {
    "datsfilipe/vesper.nvim",
    config = function()
      require("vesper").setup({})
      vim.cmd.colorscheme("vesper")
    end,
  },
}

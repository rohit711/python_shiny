from shiny import App, ui, reactive, render
import plotly.express as px

gapminder = px.data.gapminder()

app_ui = ui.page_fluid(
    ui.h2("Python Shiny - Gapminder Dashboard - "),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_slider(
                "year", "Select year", min=gapminder.year.min(),
                max=gapminder.year.max(), step=5, value=2007
            ),
            ui.output_ui("country_selector")  # dynamic country selector
        ),
        ui.panel_well(
            ui.output_ui("scatter_plot"),
            ui.output_ui("time_series"),
            ui.output_ui("pop_time_series"),
            ui.output_ui("gdp_time_series"),
        )
    )
)

def server(input, output, session):
    
    @reactive.Calc
    def filtered_data():
        return gapminder[gapminder.year == input.year()]
    
    @output()
    @render.ui
    def country_selector():
        df = filtered_data()
        countries = sorted(df['country'].unique())
        selected = ["United States", "China"]
        selected = [c for c in selected if c in countries]
        return ui.input_selectize(
            "selected_countries", "Select countries",
            choices=countries,
            multiple=True,
            selected=selected
        )
    
    @output()
    @render.ui
    def scatter_plot():
        df = filtered_data()
        fig = px.scatter(
            df,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            size_max=60,
            log_x=True,
            title=f"Life Expectancy vs GDP Per Capita in {input.year()}"
        )
        fig.update_layout(transition_duration=500)
        return ui.HTML(fig.to_html(include_plotlyjs='cdn', full_html=False))
    
    @output()
    @render.ui
    def time_series():
        selected = input.selected_countries()
        if not selected:
            return ui.HTML("<div><em>Please select at least one country to see the time series plot.</em></div>")
        df = gapminder[gapminder.country.isin(selected)]
        fig = px.line(
            df,
            x="year",
            y="lifeExp",
            color="country",
            markers=True,
            title="Life Expectancy Over Time"
        )
        fig.update_layout(transition_duration=500)
        return ui.HTML(fig.to_html(include_plotlyjs=False, full_html=False))

    @output()
    @render.ui
    def pop_time_series():
        selected = input.selected_countries()
        if not selected:
            return ui.HTML("<div><em>Please select countries to see the population over time plot.</em></div>")
        df = gapminder[gapminder.country.isin(selected)]
        fig = px.line(
            df,
            x="year",
            y="pop",
            color="country",
            markers=True,
            title="Population Over Time",
            labels={"pop": "Population"}
        )
        fig.update_layout(transition_duration=500)
        return ui.HTML(fig.to_html(include_plotlyjs=False, full_html=False))

    @output()
    @render.ui
    def gdp_time_series():
        selected = input.selected_countries()
        if not selected:
            return ui.HTML("<div><em>Please select countries to see the GDP per capita over time plot.</em></div>")
        df = gapminder[gapminder.country.isin(selected)]
        fig = px.line(
            df,
            x="year",
            y="gdpPercap",
            color="country",
            markers=True,
            title="GDP Per Capita Over Time",
            labels={"gdpPercap": "GDP Per Capita"}
        )
        fig.update_layout(transition_duration=500)
        return ui.HTML(fig.to_html(include_plotlyjs=False, full_html=False))


app = App(app_ui, server)

import plotly.graph_objects as go


class CustomeFigure(go.Figure):
    def __init__(
        self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs
    ):
        super().__init__(data, layout, frames, skip_invalid, **kwargs)
        self.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        self.update_xaxes(showgrid=False)
        self.update_yaxes(showgrid=False)
        self.update_layout(showlegend=False, margin=dict(t=0, r=0, l=0, b=0))

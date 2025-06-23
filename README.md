![Crypto_project drawio](https://github.com/user-attachments/assets/c7c87d47-6906-4c50-a7a1-8053dc327734)# 🪙 Real-Time Crypto Analytics Platform

A full-stack real-time cryptocurrency analytics platform combining **data engineering**, **machine learning**, and **interactive dashboards** — featuring anomaly detection, time-series forecasting, and sentiment analysis.


---

## 🚀 Overview

This project ingests **live cryptocurrency data** from [CoinGecko](https://coingecko.com) and [Alternative.me (Fear & Greed Index)](https://alternative.me/crypto/fear-and-greed-index/), performs real-time ETL, applies ML models for anomaly detection and forecasting, and visualizes insights in a beautiful dashboard using **Dash** and **Streamlit**.

> 🔁 Built for end-to-end data flow: `Kafka → Spark → PostgreSQL → Airflow → ML → Dash`

---

## 🏗️ Architecture

[Uploading crypto.d<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36" version="27.1.6">
  <diagram name="Page-1" id="AFdcOUHKqkFq2DwqemjB">
    <mxGraphModel dx="3271" dy="1013" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827" background="none" math="0" shadow="1">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-6" value="EC2 instance contents" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_ec2_instance_contents;strokeColor=#D86613;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#D86613;dashed=0;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="190" width="330" height="345.25" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-7" value="" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.ec2;fillColor=#F58534;gradientColor=none;shadow=1;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-6">
          <mxGeometry x="270" y="8.5" width="40" height="41.5" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-34" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-6" source="2BDDP4E5-lP9xPs0Tv10-13" target="2BDDP4E5-lP9xPs0Tv10-8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-13" value="" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#dae8fc;strokeColor=#6c8ebf;shape=mxgraph.alibaba_cloud.cloudbox;fillStyle=auto;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-6">
          <mxGeometry x="128.2" y="190" width="73.6" height="85.25" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-8" value="" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;shape=mxgraph.alibaba_cloud.kafka;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-6">
          <mxGeometry x="131.25" y="48.5" width="67.5" height="50" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-64" value="Kafka Broker&amp;nbsp;" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-6">
          <mxGeometry x="31.25" y="40" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-65" value="Kafka Producer" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-6">
          <mxGeometry x="15" y="224" width="110" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-12" value="" style="aspect=fixed;sketch=0;html=1;dashed=0;whitespace=wrap;verticalLabelPosition=bottom;verticalAlign=top;fillColor=#2875E2;strokeColor=#ffffff;points=[[0.005,0.63,0],[0.1,0.2,0],[0.9,0.2,0],[0.5,0,0],[0.995,0.63,0],[0.72,0.99,0],[0.5,1,0],[0.28,0.99,0]];shape=mxgraph.kubernetes.icon2;kubernetesLabel=1;prIcon=api;shadow=1;gradientColor=default;strokeWidth=5;" vertex="1" parent="1">
          <mxGeometry x="-30" y="305.02" width="120" height="115.2" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-77" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;shadow=1;flowAnimation=1;" edge="1" parent="1" source="2BDDP4E5-lP9xPs0Tv10-30" target="2BDDP4E5-lP9xPs0Tv10-49">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-30" value="EC2 instance contents" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_ec2_instance_contents;strokeColor=#D86613;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#D86613;dashed=0;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="730" y="90" width="690" height="570" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-31" value="" style="outlineConnect=0;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws3.ec2;fillColor=#F58534;gradientColor=none;shadow=1;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="630" y="10" width="40" height="50" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-9" value="" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/other/Arc_PostgreSQL.svg;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="280" y="430" width="114.84" height="120" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-10" value="" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#FF6A00;strokeColor=none;shape=mxgraph.alibaba_cloud.spark_data_insights;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="80" y="150" width="92.21" height="100" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-38" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.084;entryY=0.72;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="-269" y="170" as="sourcePoint" />
            <mxPoint x="79.9956400000001" y="202" as="targetPoint" />
            <Array as="points">
              <mxPoint x="-97.75" y="170" />
              <mxPoint x="-97.75" y="202" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-79" value="&amp;nbsp; &amp;nbsp; Spark&amp;nbsp; &amp;nbsp;&amp;nbsp;&lt;br&gt;Streaming&lt;div&gt;&lt;br/&gt;&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="2BDDP4E5-lP9xPs0Tv10-38">
          <mxGeometry x="0.1549" y="-1" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-41" value="" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#FF6A00;strokeColor=none;shape=mxgraph.alibaba_cloud.spark_data_insights;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="291.32" y="150" width="92.21" height="100" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-42" value="" style="points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;fillColor=#FF6A00;strokeColor=none;shape=mxgraph.alibaba_cloud.spark_data_insights;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="500" y="150" width="92.21" height="100" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-44" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.003;entryY=0.477;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-30" source="2BDDP4E5-lP9xPs0Tv10-10" target="2BDDP4E5-lP9xPs0Tv10-9">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="126" y="487" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-46" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.489;entryY=1.011;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-30" source="2BDDP4E5-lP9xPs0Tv10-9" target="2BDDP4E5-lP9xPs0Tv10-41">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-47" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-30" source="2BDDP4E5-lP9xPs0Tv10-9">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="549" y="250" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-48" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.977;entryY=0.815;entryDx=0;entryDy=0;entryPerimeter=0;exitX=0.971;exitY=0.684;exitDx=0;exitDy=0;exitPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="2BDDP4E5-lP9xPs0Tv10-30" source="2BDDP4E5-lP9xPs0Tv10-42" target="2BDDP4E5-lP9xPs0Tv10-9">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="804.6800000000001" y="210" as="sourcePoint" />
            <mxPoint x="609.9956399999999" y="512.6400000000001" as="targetPoint" />
            <Array as="points">
              <mxPoint x="610" y="218" />
              <mxPoint x="610" y="528" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-62" value="" style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/png,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAYAAAA+s9J6AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAEumlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4KPHg6eG1wbWV0YSB4bWxuczp4PSdhZG9iZTpuczptZXRhLyc+CjxyZGY6UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4bWxuczpBdHRyaWI9J2h0dHA6Ly9ucy5hdHRyaWJ1dGlvbi5jb20vYWRzLzEuMC8nPgogIDxBdHRyaWI6QWRzPgogICA8cmRmOlNlcT4KICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0nUmVzb3VyY2UnPgogICAgIDxBdHRyaWI6Q3JlYXRlZD4yMDI1LTA2LTIzPC9BdHRyaWI6Q3JlYXRlZD4KICAgICA8QXR0cmliOkV4dElkPjFlZjllYmMxLTZmMDctNGM3NS05ZDhmLTdiMGZiNjE4ZmNjZDwvQXR0cmliOkV4dElkPgogICAgIDxBdHRyaWI6RmJJZD41MjUyNjU5MTQxNzk1ODA8L0F0dHJpYjpGYklkPgogICAgIDxBdHRyaWI6VG91Y2hUeXBlPjI8L0F0dHJpYjpUb3VjaFR5cGU+CiAgICA8L3JkZjpsaT4KICAgPC9yZGY6U2VxPgogIDwvQXR0cmliOkFkcz4KIDwvcmRmOkRlc2NyaXB0aW9uPgoKIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PScnCiAgeG1sbnM6ZGM9J2h0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvJz4KICA8ZGM6dGl0bGU+CiAgIDxyZGY6QWx0PgogICAgPHJkZjpsaSB4bWw6bGFuZz0neC1kZWZhdWx0Jz5VbnRpdGxlZCBkZXNpZ24gLSAxPC9yZGY6bGk+CiAgIDwvcmRmOkFsdD4KICA8L2RjOnRpdGxlPgogPC9yZGY6RGVzY3JpcHRpb24+CgogPHJkZjpEZXNjcmlwdGlv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;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="302.42" y="20" width="70" height="70" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-67" value="Bronze Job" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="86.11000000000001" y="120" width="80" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-68" value="Silver Anomaly Job" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="272.42" y="120" width="130" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-69" value="Forecast Prophet Job" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="476.11" y="120" width="140" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-73" value="Postgres" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;rounded=1;" vertex="1" parent="2BDDP4E5-lP9xPs0Tv10-30">
          <mxGeometry x="302.42" y="400" width="70" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-37" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.502;entryY=0.943;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="1" source="2BDDP4E5-lP9xPs0Tv10-12" target="2BDDP4E5-lP9xPs0Tv10-13">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="30" y="477" />
              <mxPoint x="435" y="477" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-76" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2BDDP4E5-lP9xPs0Tv10-49" target="2BDDP4E5-lP9xPs0Tv10-70">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-49" value="" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/general/Dashboard2.svg;" vertex="1" parent="1">
          <mxGeometry x="790" y="750" width="113.34" height="80" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-75" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="2BDDP4E5-lP9xPs0Tv10-52" target="2BDDP4E5-lP9xPs0Tv10-72">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-52" value="" style="image;aspect=fixed;html=1;points=[];align=center;fontSize=12;image=img/lib/azure2/other/Azure_Monitor_Dashboard.svg;" vertex="1" parent="1">
          <mxGeometry x="1280" y="750" width="100.76" height="93.64" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-66" value="Coingecko API" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="-20" y="270" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-70" value="Dash Dashboard (Forecast,Anomalies,Sentiment)&amp;nbsp;" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="701.67" y="880" width="290" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-72" value="Streamlit Dashboard (KPIs,Anomalies,Sentiment)" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;shadow=1;glass=1;sketch=1;curveFitting=1;jiggle=2;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
          <mxGeometry x="1185.38" y="880" width="290" height="30" as="geometry" />
        </mxCell>
        <mxCell id="2BDDP4E5-lP9xPs0Tv10-78" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.638;entryY=0.036;entryDx=0;entryDy=0;entryPerimeter=0;shadow=1;flowAnimation=1;" edge="1" parent="1" source="2BDDP4E5-lP9xPs0Tv10-30" target="2BDDP4E5-lP9xPs0Tv10-52">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
rawio…]()









---

## 🔧 Tech Stack

| Layer          | Technologies Used                                      |
|----------------|--------------------------------------------------------|
| **Ingestion**   | Kafka, Python Kafka Producer, CoinGecko API            |
| **ETL**         | Apache Spark Structured Streaming, PySpark             |
| **Database**    | PostgreSQL (Bronze, Silver, Anomaly, Sentiment Layers) |
| **ML Models**   | Isolation Forest, Prophet (Forecasting), LOF (Planned) |
| **Scheduler**   | Apache Airflow                                         |
| **Dashboard**   | Dash (Plotly), Streamlit                               |
| **Infra**       | AWS EC2, systemd                     |

---

## 📊 Features

✅ Real-time crypto price streaming from CoinGecko  
✅ Spark Streaming-based ETL to PostgreSQL  
✅ Anomaly detection using Isolation Forest  
✅ Time-series price forecasting using Prophet  
✅ Sentiment analysis via Fear & Greed Index API  
✅ Interactive Dash dashboard with:
- 📈 Price & anomaly overlay
- 🔮 Forecast prediction
- 🌙 Dark mode
- 📥 CSV download
- 🎭 Date range picker  
✅ Streamlit version available with heatmaps and autorefresh

---

---

## 📈 ML Capabilities

### 🔍 Anomaly Detection

- **Model**: Isolation Forest (`scikit-learn`)
- **Input Features**:
  - `avg_price`
  - `avg_volume`
  - `market_cap`
  - `24h price change %`
- **Labeling**: Normal (1), Anomaly (-1)
- **Storage**: Stored in `anomaly.<coin>_anomalies`

> 📌 Supports expansion to LOF or One-Class SVM

### 📉 Forecasting

- **Model**: [Facebook Prophet](https://facebook.github.io/prophet/)
- **Predicted Feature**: Future `avg_price`
- **Visuals**:
  - Forecast line with 95% confidence bounds
- **Storage**: `silver_crypto.forecast_price`

---

## 😱 Sentiment Analysis

- Source: [Alternative.me Crypto Fear & Greed Index](https://alternative.me/crypto/fear-and-greed-index/)
- API: `https://api.alternative.me/fng/`
- Stored to: `sentiment_crypto.fear_greed_index`
- Dashboard Integration: Dual Y-axis chart (price + sentiment)

---

## 📺 Dash UI Highlights

- 🌙 **Dark Mode** toggle  
- 🔮 **Show Forecast** toggle  
- 📉 Price + anomaly markers  
- 📤 Export CSV  
- 📅 Date filtering  
- 📊 Fear & Greed sentiment overlay  
- 🪙 Logo-rich dropdown with 5 top coins (BTC, ETH, USDT, XRP, SOL)

---



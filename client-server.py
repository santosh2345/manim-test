from manim import *
import random

class ClientServerArchitecture(Scene):
    def construct(self):
        # Title
        title = Text("Client-Server Architecture", font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(1)
        
        # Create clients (mobile, desktop, browser)
        clients = self.create_clients()
        self.play(FadeIn(clients), run_time=2)
        self.wait(1)
        
        # Create internet cloud
        internet = self.create_internet()
        self.play(Create(internet), run_time=2)
        self.wait(1)
        
        # Create load balancer
        load_balancer = self.create_load_balancer()
        self.play(FadeIn(load_balancer), run_time=2)
        self.wait(1)
        
        # Create web servers
        web_servers = self.create_web_servers()
        self.play(FadeIn(web_servers), run_time=2)
        self.wait(1)
        
        # Create application servers
        app_servers = self.create_app_servers()
        self.play(FadeIn(app_servers), run_time=2)
        self.wait(1)
        
        # Create cache layer
        cache = self.create_cache()
        self.play(FadeIn(cache), run_time=2)
        self.wait(1)
        
        # Create database cluster
        databases = self.create_databases()
        self.play(FadeIn(databases), run_time=2)
        self.wait(1)
        
        # Create CDN
        cdn = self.create_cdn()
        self.play(FadeIn(cdn), run_time=2)
        self.wait(1)
        
        # Animate data flow
        self.animate_data_flow(clients, internet, load_balancer, web_servers, app_servers, cache, databases, cdn)
        
        # Show scaling animation
        self.animate_scaling(web_servers, app_servers)
        
        # Show caching benefits
        self.animate_caching_benefits(clients, cache, databases)
        
        # Final overview
        self.show_final_overview()
        
        self.wait(3)
    
    def create_clients(self):
        # Create different types of clients
        mobile = Rectangle(width=0.6, height=1.0, color=GREEN, fill_opacity=0.3)
        mobile_text = Text("Mobile", font_size=16).move_to(mobile.get_center())
        mobile_group = VGroup(mobile, mobile_text).shift(LEFT * 6 + UP * 2)
        
        desktop = Rectangle(width=1.2, height=0.8, color=GREEN, fill_opacity=0.3)
        desktop_text = Text("Desktop", font_size=16).move_to(desktop.get_center())
        desktop_group = VGroup(desktop, desktop_text).shift(LEFT * 6)
        
        browser = Rectangle(width=1.0, height=0.6, color=GREEN, fill_opacity=0.3)
        browser_text = Text("Browser", font_size=16).move_to(browser.get_center())
        browser_group = VGroup(browser, browser_text).shift(LEFT * 6 + DOWN * 2)
        
        clients_label = Text("CLIENTS", font_size=20, color=GREEN).shift(LEFT * 6 + DOWN * 3)
        
        return VGroup(mobile_group, desktop_group, browser_group, clients_label)
    
    def create_internet(self):
        # Internet cloud
        cloud = Ellipse(width=2, height=1.2, color=BLUE, fill_opacity=0.2)
        cloud_text = Text("Internet", font_size=18, color=BLUE)
        cloud_group = VGroup(cloud, cloud_text).shift(LEFT * 3.5)
        return cloud_group
    
    def create_load_balancer(self):
        # Load balancer
        lb_rect = Rectangle(width=1.5, height=1, color=YELLOW, fill_opacity=0.4)
        lb_text = Text("Load\nBalancer", font_size=16).move_to(lb_rect.get_center())
        lb_group = VGroup(lb_rect, lb_text).shift(LEFT * 1)
        
        # Add arrows showing distribution
        arrow1 = Arrow(start=lb_rect.get_right(), end=lb_rect.get_right() + RIGHT * 0.5 + UP * 0.5, color=YELLOW)
        arrow2 = Arrow(start=lb_rect.get_right(), end=lb_rect.get_right() + RIGHT * 0.5, color=YELLOW)
        arrow3 = Arrow(start=lb_rect.get_right(), end=lb_rect.get_right() + RIGHT * 0.5 + DOWN * 0.5, color=YELLOW)
        
        return VGroup(lb_group, arrow1, arrow2, arrow3)
    
    def create_web_servers(self):
        # Multiple web servers
        servers = VGroup()
        for i in range(3):
            server = Rectangle(width=0.8, height=1, color=ORANGE, fill_opacity=0.3)
            server_text = Text(f"Web\nServer {i+1}", font_size=14).move_to(server.get_center())
            server_group = VGroup(server, server_text).shift(UP * (1 - i) + RIGHT * 1.5)
            servers.add(server_group)
        
        web_label = Text("WEB SERVERS", font_size=16, color=ORANGE).shift(RIGHT * 1.5 + DOWN * 2.5)
        return VGroup(servers, web_label)
    
    def create_app_servers(self):
        # Application servers
        app_servers = VGroup()
        for i in range(2):
            server = Rectangle(width=1, height=0.8, color=RED, fill_opacity=0.3)
            server_text = Text(f"App\nServer {i+1}", font_size=14).move_to(server.get_center())
            server_group = VGroup(server, server_text).shift(UP * (0.5 - i) + RIGHT * 3.5)
            app_servers.add(server_group)
        
        app_label = Text("APP SERVERS", font_size=16, color=RED).shift(RIGHT * 3.5 + DOWN * 2)
        return VGroup(app_servers, app_label)
    
    def create_cache(self):
        # Cache layer (Redis/Memcached)
        cache_rect = Rectangle(width=1.2, height=0.6, color=PURPLE, fill_opacity=0.4)
        cache_text = Text("Cache\n(Redis)", font_size=14, color=WHITE).move_to(cache_rect.get_center())
        cache_group = VGroup(cache_rect, cache_text).shift(RIGHT * 5.5 + UP * 1)
        
        cache_label = Text("CACHE LAYER", font_size=16, color=PURPLE).shift(RIGHT * 5.5 + UP * 0.3)
        return VGroup(cache_group, cache_label)
    
    def create_databases(self):
        # Database cluster
        primary_db = Rectangle(width=1, height=0.8, color=TEAL, fill_opacity=0.4)
        primary_text = Text("Primary\nDB", font_size=12).move_to(primary_db.get_center())
        primary_group = VGroup(primary_db, primary_text).shift(RIGHT * 5 + DOWN * 1)
        
        replica1 = Rectangle(width=0.8, height=0.6, color=TEAL, fill_opacity=0.2)
        replica1_text = Text("Replica\n1", font_size=10).move_to(replica1.get_center())
        replica1_group = VGroup(replica1, replica1_text).shift(RIGHT * 6 + DOWN * 1.5)
        
        replica2 = Rectangle(width=0.8, height=0.6, color=TEAL, fill_opacity=0.2)
        replica2_text = Text("Replica\n2", font_size=10).move_to(replica2.get_center())
        replica2_group = VGroup(replica2, replica2_text).shift(RIGHT * 6 + DOWN * 0.5)
        
        db_label = Text("DATABASE CLUSTER", font_size=16, color=TEAL).shift(RIGHT * 5.5 + DOWN * 2.5)
        
        # Replication arrows
        repl_arrow1 = Arrow(start=primary_db.get_right(), end=replica1.get_left(), color=TEAL, stroke_width=2)
        repl_arrow2 = Arrow(start=primary_db.get_right(), end=replica2.get_left(), color=TEAL, stroke_width=2)
        
        return VGroup(primary_group, replica1_group, replica2_group, db_label, repl_arrow1, repl_arrow2)
    
    def create_cdn(self):
        # CDN nodes
        cdn_nodes = VGroup()
        positions = [
            LEFT * 2 + UP * 3.5,
            RIGHT * 2 + UP * 3.5,
            LEFT * 4 + DOWN * 3.5,
            RIGHT * 4 + DOWN * 3.5
        ]
        
        for i, pos in enumerate(positions):
            node = Circle(radius=0.3, color=PINK, fill_opacity=0.3)
            node_text = Text(f"CDN\n{i+1}", font_size=10).move_to(node.get_center())
            node_group = VGroup(node, node_text).shift(pos)
            cdn_nodes.add(node_group)
        
        cdn_label = Text("CDN NODES", font_size=16, color=PINK).shift(DOWN * 3.8)
        return VGroup(cdn_nodes, cdn_label)
    
    def animate_data_flow(self, clients, internet, load_balancer, web_servers, app_servers, cache, databases, cdn):
        # Animate request flow
        flow_label = Text("Request Flow Animation", font_size=24, color=WHITE)
        flow_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(self.mobjects[0], flow_label))
        
        # Create animated dots for requests
        for _ in range(3):
            # Request from client to internet
            dot = Dot(color=YELLOW).move_to(clients[0].get_center())
            self.add(dot)
            self.play(dot.animate.move_to(internet.get_center()), run_time=0.8)
            
            # Internet to load balancer
            self.play(dot.animate.move_to(load_balancer[0].get_center()), run_time=0.8)
            
            # Load balancer to random web server
            server_choice = random.randint(0, 2)
            target_server = web_servers[0][server_choice]
            self.play(dot.animate.move_to(target_server.get_center()), run_time=0.8)
            
            # Web server to app server
            app_choice = random.randint(0, 1)
            target_app = app_servers[0][app_choice]
            self.play(dot.animate.move_to(target_app.get_center()), run_time=0.8)
            
            # Check cache first
            self.play(dot.animate.move_to(cache[0].get_center()), run_time=0.6)
            
            # If not in cache, go to database
            if random.choice([True, False]):  # 50% cache hit
                cache_hit = Text("Cache HIT!", font_size=16, color=GREEN)
                cache_hit.next_to(cache[0], UP)
                self.play(FadeIn(cache_hit), run_time=0.5)
                self.play(FadeOut(cache_hit), run_time=0.5)
            else:
                cache_miss = Text("Cache MISS", font_size=16, color=RED)
                cache_miss.next_to(cache[0], UP)
                self.play(FadeIn(cache_miss), run_time=0.5)
                self.play(FadeOut(cache_miss), run_time=0.5)
                self.play(dot.animate.move_to(databases[0].get_center()), run_time=0.8)
                self.play(dot.animate.move_to(cache[0].get_center()), run_time=0.8)  # Store in cache
            
            # Response back to client
            self.play(dot.animate.move_to(target_app.get_center()), run_time=0.6)
            self.play(dot.animate.move_to(target_server.get_center()), run_time=0.6)
            self.play(dot.animate.move_to(load_balancer[0].get_center()), run_time=0.6)
            self.play(dot.animate.move_to(internet.get_center()), run_time=0.6)
            self.play(dot.animate.move_to(clients[0].get_center()), run_time=0.6)
            
            self.remove(dot)
            self.wait(0.5)
    
    def animate_scaling(self, web_servers, app_servers):
        scaling_label = Text("Auto-Scaling Animation", font_size=24, color=WHITE)
        scaling_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(self.mobjects[0], scaling_label))
        
        # Show high load
        load_indicator = Text("HIGH LOAD DETECTED!", font_size=20, color=RED)
        load_indicator.shift(UP * 2)
        self.play(FadeIn(load_indicator), run_time=1)
        
        # Add new server instances
        new_web_server = Rectangle(width=0.8, height=1, color=ORANGE, fill_opacity=0.3)
        new_web_text = Text("Web\nServer 4", font_size=14).move_to(new_web_server.get_center())
        new_web_group = VGroup(new_web_server, new_web_text).shift(DOWN * 2 + RIGHT * 1.5)
        
        self.play(FadeIn(new_web_group), run_time=2)
        
        new_app_server = Rectangle(width=1, height=0.8, color=RED, fill_opacity=0.3)
        new_app_text = Text("App\nServer 3", font_size=14).move_to(new_app_server.get_center())
        new_app_group = VGroup(new_app_server, new_app_text).shift(DOWN * 1.5 + RIGHT * 3.5)
        
        self.play(FadeIn(new_app_group), run_time=2)
        
        # Show load balanced
        balanced_indicator = Text("LOAD BALANCED", font_size=20, color=GREEN)
        balanced_indicator.shift(UP * 2)
        self.play(Transform(load_indicator, balanced_indicator), run_time=1)
        self.wait(2)
        self.play(FadeOut(load_indicator), FadeOut(new_web_group), FadeOut(new_app_group))
    
    def animate_caching_benefits(self, clients, cache, databases):
        benefits_label = Text("Caching Benefits", font_size=24, color=WHITE)
        benefits_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(self.mobjects[0], benefits_label))
        
        # Show performance metrics
        metrics = VGroup(
            Text("Response Time: 50ms → 5ms", font_size=16, color=GREEN),
            Text("Database Load: ↓ 80%", font_size=16, color=GREEN),
            Text("Throughput: ↑ 10x", font_size=16, color=GREEN)
        ).arrange(DOWN).shift(LEFT * 2)
        
        self.play(FadeIn(metrics), run_time=2)
        
        # Show cache warming
        warming_text = Text("Cache Warming...", font_size=16, color=YELLOW)
        warming_text.next_to(cache[0], DOWN)
        self.play(FadeIn(warming_text), run_time=1)
        
        # Animate cache filling up
        cache_fill = Rectangle(width=1.2, height=0.6, color=PURPLE, fill_opacity=0.8)
        cache_fill.move_to(cache[0][0].get_center())
        self.play(DrawBorderThenFill(cache_fill), run_time=2)
        
        warmed_text = Text("Cache Ready!", font_size=16, color=GREEN)
        self.play(Transform(warming_text, warmed_text), run_time=1)
        
        self.wait(2)
        self.play(FadeOut(metrics), FadeOut(warming_text), FadeOut(cache_fill))
    
    def show_final_overview(self):
        final_label = Text("Complete System Architecture", font_size=24, color=WHITE)
        final_label.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(self.mobjects[0], final_label))
        
        # Show system benefits
        benefits = VGroup(
            Text("✓ High Availability", font_size=16, color=GREEN),
            Text("✓ Scalability", font_size=16, color=GREEN),
            Text("✓ Performance", font_size=16, color=GREEN),
            Text("✓ Fault Tolerance", font_size=16, color=GREEN),
            Text("✓ Load Distribution", font_size=16, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(RIGHT * 0.5)
        
        self.play(FadeIn(benefits), run_time=3)
        
        # Simple final animation - just fade all components
        self.play(
            *[FadeOut(mob, shift=DOWN) for mob in self.mobjects[1:] if mob != benefits],
            run_time=3
        )
        
        # Final message
        final_msg = Text("Architecture Complete!", font_size=32, color=GOLD)
        final_msg.move_to(ORIGIN)
        self.play(Write(final_msg), run_time=2)
        
        self.wait(2)